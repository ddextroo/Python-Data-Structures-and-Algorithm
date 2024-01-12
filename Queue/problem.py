
class Node:
    def __init__(self, data, priority) -> None:
        self.data = data
        self.next = None 
        self.priority = priority
class Queue:
    def __init__(self) -> None:
        self.front = self.rear = None
    def enqueue(self, data, priority=None):
        node = Node(data, priority)
        
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
        if current.next.next is None and current.priority == current.next.priority:
            self.rear = node
            
    def dequeue(self):
        if self.front is None:
            return "hehe"
        removed = self.front.data
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None
        return removed
    def get_front(self):
        return self.front.data if self.front else None
    def get_rear(self):
        return self.rear.data if self.rear else None
    def display(self):
        current = self.front
        while current:
            print(current.data, current.priority)
            current = current.next
q = Queue()
q.enqueue(2)
q.enqueue(4)
q.enqueue(2,0)
q.enqueue(4,1)
q.display()