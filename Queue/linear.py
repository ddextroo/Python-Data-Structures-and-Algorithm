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
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            return "Queue is empty"
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

        if self.front is None:
            print("Queue is empty")
        else:
            while current:
                print(current.data, end=" ")
                current = current.next


q = Queue()
q.enqueue(7)
q.enqueue(3)
q.enqueue(8)
q.enqueue(5)
q.dequeue()
q.dequeue()
q.dequeue()
q.display()
print()
print("Front: ", q.get_front())
print("Rear: ", q.get_rear())
