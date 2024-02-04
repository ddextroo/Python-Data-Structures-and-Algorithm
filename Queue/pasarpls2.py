class Node:
    def __init__(self, task_name, priority) -> None:
        self.task_name = task_name
        self.priority = priority
        self.next = None
class Task:
    def __init__(self) -> None:
        self.front = self.rear = None
    def add_task(self, task_name, priority=None):
        node = Node(task_name, priority)
        if self.front is None or self.rear is None:
            self.front = self.rear = node
            return
        if priority is None or self.rear.priority and priority > self.rear.priority:
            self.rear.next = node
            self.rear = node
            return
        if self.front.priority is None or self.front.priority and priority < self.front.priority:
            node.next = self.front
            self.front = node
            return
        current = self.front
        while current.next:
            if current.next.priority is None or priority <= current.next.priority:
                break
            current = current.next
        temp = current.next
        current.next = node
        node.next = temp
        if current.next.next is None and priority == current.next.priority:
            self.rear = node
    def get_front(self):
        return self.front.task_name if self.front else None
    def get_rear(self):
        return self.rear.task_name if self.rear else None
    def get_task(self):
        current = self.front
        
        while current:
            print(current.task_name, current.priority)
            current = current.next
    def complete_task(self):
        if self.front is None:
            return "Empty"
        removed = self.front.task_name
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        return removed
    def change_task(self, task_name, new_priority):
        current = self.front
        
        if self.front.task_name == task_name:
            self.front = self.front.next
            self.add_task(task_name, new_priority)
        else:
            while current.task_name != task_name:
                pre_current = current
                current = current.next
            if self.rear.task_name == task_name:
                pre_current.next = None
                self.rear = pre_current
            else:
                pre_current.next = current.next
            self.add_task(task_name, new_priority)

t = Task()
t.add_task(2,4)
t.add_task(5,4)
t.add_task(7,7)
t.add_task(8,2)
t.add_task(1,5)
t.change_task(7, 1)
 
t.get_task()
