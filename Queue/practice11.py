class Node:
    def _init_ (self, data, priority=None):
        self.data = data
        self.priority = priority
        self.next = None
class Queue:
    def __init__(self):
        self.front = self.rear = None
    
    def enqueue(self, data, priority=None):
        node = Node(data, priority)
        current = self.front
        
        if self.is_empty():
            self.front = self.rear = node
        else:
            if self.front.priority is None:
                node.next = self.front
                self.front = node
                return
            if priority is None:
                self.rear.next = node
                self.rear = self.rear.next
                return
            elif priority < self.front.priority:
                node.next = self.front
                self.front = node
                return
            elif self.rear.priority and priority > self.rear.priority:
                self.rear.next = node
                self.rear = self.rear.next
                return
            else:
                while current.next:
                    if current.next.priority is None or priority < current.next.priority:
                        break
                    current = current.next
                node.next = current.next
                current.next = node
             
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            self.front = self.front.next
    def get_front(self):
        return self.front.data if self.front else None
    def get_rear(self):
        return self.rear.data if self.rear else None
    def is_empty(self):
        return self.front is None
    def display(self):
        current = self.front
        
        while current:
            print(f'data = {current.data}\tpriority = {current.priority}')
            current = current.next
        print()
    def size(self):
        current = self.front
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    def concatenate(self, l):
        head_copy = l.front
        while head_copy:
            self.enqueue(head_copy.data)
            head_copy = head_copy.next  