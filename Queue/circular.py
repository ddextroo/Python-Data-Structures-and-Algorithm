class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        node = Node(data)

        if self.rear is None:
            self.front = self.rear = node
            self.rear.next = self.front
        else:
            self.rear.next = node
            self.rear = node
            self.rear.next = self.front

    def dequeue(self):
        if self.front is None:
            return "Queue is empty"
        else:
            self.front = self.front.next
            self.rear.next = self.front

    def get_front(self):
        return self.front.data if self.front else None
 
    def get_rear(self):
        return self.rear.data if self.rear else None

    def check(self):
        return self.rear.next.data if self.rear.next else None

    def display(self):
        current = self.front

        while current.next != self.front:
            print(current.data, end=" ")
            current = current.next
        print(current.data, end=" ")

    def is_empty(self):
        return True if self.get_front() else False

q = Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(5)
q.display()
print()
q.dequeue()
q.dequeue()
q.dequeue()
q.enqueue(9)
q.display()
