class Node:
    def __init__(self, name, urgency) -> None:
        self.name = name
        self.next = None
        self.urgency = urgency
        self.urgency_number = self.get_urgency_number()

    def get_urgency_number(self):
        if self.urgency == "critical":
            return 1
        elif self.urgency == "serious":
            return 2
        elif self.urgency == "moderate":
            return 3


class Queue:
    def __init__(self) -> None:
        self.front = self.rear = None
        self.patients_cured = 0

    def add_patient(self, name, urgency="moderate"):
        node = Node(name, urgency)
        if self.front is None and self.rear is None:
            self.front = self.rear = node
            return
        if node.urgency_number > self.rear.urgency_number:
            self.rear.next = node
            self.rear = node
            return
        if node.urgency_number < self.front.urgency_number:
            node.next = self.front
            self.front = node
            return
        current = self.front
        while current.next:
            if node.urgency_number <= current.next.urgency_number:
                break
            current = current.next
        temp = current.next
        current.next = node
        node.next = temp
        if current.next.next is None and current.urgency_number == current.next.urgency_number:
            self.rear = node

    def dequeue(self):
        if self.front is None:
            return "queue is empty"
        removed = self.front.name
        self.front = self.front.next
        self.patients_cured += 1
        if self.front is None:
            self.rear = None
        return removed
    
    def evaluate_patient(self, urgency):
        if self.front is None:
            return "queue is empty"
        removed = self.front.name
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.add_patient(removed, urgency)
        

    def get_front(self):
        return self.front.name if self.front else None

    def get_rear(self):
        return self.rear.name if self.rear else None
    def track(self):
        return self.patients_cured if self.patients_cured else 0

    def display(self):
        current = self.front
        while current:
            print(current.name, current.urgency)
            current = current.next


q = Queue()
q.add_patient("jeff", "serious")
q.add_patient("dexter", "moderate")
q.add_patient("amoshbt")
q.add_patient("amo7bt", "serious")
q.add_patient("amobt", "critical")
q.add_patient("amobweqwt", "critical")
q.display()
print()
print(q.get_front(), q.get_rear())
q.evaluate_patient("serious")
print()
print()
print()
q.display()
q.dequeue()
q.dequeue()
print(q.track())
