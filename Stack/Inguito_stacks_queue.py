
#Creating node for the applications
class Node:
    def __init__(self, name, schedule=None) -> None:
        self.name = name
        self.schedule = schedule
        self.next = None
#Stack class
class Stack:
    #initialize stack
    def __init__(self) -> None:
        self.top = None
    #push the items in the stack
    def push(self, name):
        node = Node(name)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
    #pulling them and return the latest pulled item
    def pop(self):
        if self.top is None:
            return "Stack is empty"
        removed = self.top.name
        self.top = self.top.next
        return removed
    #display the items
    def display(self):
        current = self.top
        while current:
            print(current.name)
            current = current.next
    #get the top of the stack
    def peek(self):
        return self.top.name if self.top else None

#Class Queue
class Queue:
    #initialize queue
    def __init__(self) -> None:
        self.front = self.rear = None
    #enqueue the items
    def enqueue(self, name, schedule=None):
        node = Node(name, schedule)

        #if it is empty, just put the node
        if self.front is None:
            self.front = self.rear = node
        else:
            #put at the rear
            self.rear.next = node
            self.rear = node
            return
    
    #dequeue the items in front
    def dequeue(self):
        if self.front is None:
            return "Empty"
        removed = self.front.name
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        #return the dequeue item
        return removed
    #display the queue items
    def display(self):
        current = self.front
        #traverse and get the items based on order
        while current:
            if current.schedule is None:
                print(current.name)
            else:
                print(current.name, current.schedule)
            current = current.next

#initialization of classes
inbox = Queue()
reviewing = Stack()
interview = Queue()
hiring = Stack()
#inbox
print("Inbox: ")
inbox.enqueue("Barista")
inbox.enqueue("Person")
inbox.enqueue("Human")
inbox.enqueue("People")
inbox.enqueue("Species")
inbox.display()
print()
print()
#reviewing
print("Reviewing: ")
reviewing.push(inbox.dequeue())
reviewing.push(inbox.dequeue())
reviewing.push(inbox.dequeue())
reviewing.display()
print()
print()
#remaining
print("Remaining: ")
inbox.display()
print()
print()
print()
#interview
print("Interview: ")
interview.enqueue(reviewing.pop(), "Tuesday - Bring CV and Resume")
interview.enqueue(reviewing.pop(), "Saturday - Bring CV and Resume")
interview.display()
print()
print("Remaining: ")
reviewing.display()
print()
#hiring decision
print("Hiring Decision: ")
hiring.push(interview.dequeue())
hiring.push(interview.dequeue())
hiring.display()
print()
print()
