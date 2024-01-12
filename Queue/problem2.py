class Node:
    def __init__(self, data, priority=None) -> None:
        self.data = data
        self.next = None
        self.priority = priority
class Jobs:
    def __init__(self) -> None:
        self.front = self.rear = None
    def enqueue(self, job, priority="regular"):
        node = Node(job, priority)
        if self.front is None and self.rear is None:
            self.front = self.rear = node
            return
        if priority == "regular":
            self.rear.next = node
            self.rear = node
            return
        if priority == "high":
            node.next = self.front
            self.front = node
            return
    def get_front(self):
        return self.front.data if self.front else None
    def get_rear(self):
        return self.rear.data if self.rear else None
    def display(self):
        current = self.front
        while current:
            print(current.data, current.priority)
            current = current.next
j = Jobs()
j.enqueue("Job2", "high")
j.enqueue("Job1", "regular")
j.enqueue("Job4", "high")
j.enqueue("Job5", "high")
j.enqueue("Job3", "regular")
j.display()
print()
print(j.get_front())
print(j.get_rear())