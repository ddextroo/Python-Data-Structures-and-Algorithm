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
        if current.next.next.priority is None and current.priority == current.next.priority:
            self.rear = node
    def complete_task(self):
        if self.front is None:
            return "Task is empty"
        remove = self.front.task_name
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None
        return remove
    def get_next_task(self):
        return self.front.task_name if self.front else None
    def view_task_queue(self):
        current = self.front
        
        while current:
            print("Task:", current.task_name, "\tPriority:", current.priority)
            current = current.next
    def change_task_priority(self, task_name, new_priority=None):
        current = self.front
        
        if self.front.task_name == task_name:
            self.front = self.front.next
            self.add_task(current.task_name, new_priority)
        else:
            while current.task_name != task_name:
                pre_current = current
                current = current.next
            if self.rear.task_name == current.task_name:
                pre_current.next = None
                self.rear = pre_current
            else: 
                pre_current.next = current.next
            self.add_task(current.task_name, new_priority)
            
            
t = Task()
t.add_task("Washing dishes", 2)
t.add_task("Sweeping", 5)
t.add_task("Cooking", 6)
t.add_task("Sleeping", 8)
t.add_task("Washing clothes", 3)
t.add_task("Eating")
t.view_task_queue()
t.change_task_priority("Eating", 1)
print()
print()
t.view_task_queue()
            
        