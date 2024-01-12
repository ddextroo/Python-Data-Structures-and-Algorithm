class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self,data):
        node = Node(data)
        
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
    
    def pop(self):
        if self.top is None:
            return 'Stack is empty'
        else:
            popped_data = self.top
            self.top = self.top.next
            return popped_data.data
    
    def peek(self):
        return self.top.data if self.top is not None else None
    
    def reverse(self):
        temp = Stack()
        
        while self.peek():
            temp.push(self.pop())
        self.top = temp.top
    
    def copy(self, numlist):
        while self.peek():
            numlist.push(self.pop())
        numlist.reverse()
    
    def remove_duplicate(self):
        temp = Stack()
        
        while self.peek():
            if self.peek() == self.data:
                temp.push(self.pop())
        
    def display(self):
        current = self.top
        
        while current:
            print(current.data, end=" ")
            current = current.next

s = Stack()
s.push(5)
s.push(4)
s.push(3)
s.push(2)
s.push(1)
s.display()
print()

s1 = Stack()
s.copy(s1)
s1.display()

print()
s1.push(3)
s1.push(5)
s1.display()