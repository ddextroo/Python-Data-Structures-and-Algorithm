class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, data):
        node = Node(data)
        
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
            
    def pop(self):
        if self.top is None:
            return "Stack is empty"
        else:
            removed = self.top.data
            self.top = self.top.next
        return removed
    
    def peek(self):
        if self.top is None:
            return None
        else:
            return self.top.data
        # return self.top.data if not None else None
    
    def display(self):
        current = self.top
        
        while current:
            print(current.data, end=" ")
            current = current.next
    def count(self):
        current = self.top
        count = 0
        while current:
            count += 1
            current = current.next
        return count
            
    def backtrack(self):
            while self.peek():
                if self.peek() > 0:
                    i = 0
                    while i < 5:
                        print(s.pop(), end=" ")
                        if i != 4 and self.peek() < 0:
                            j = 0
                            while j < (4-i):
                                if self.peek() < 0:
                                    self.pop()
                                print(self.pop())
                                j += 1
                            print()
                            print("Error")
                            return
                        i += 1
                else:
                    s.pop()
                    print()
                    
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(-1)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.push(9)
s.push(10)
s.push(-2)
s.push(11)
s.push(12)
s.push(-3)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)


# s.display()
print()
print()
print("Backtrack:")
s.backtrack()

print() 
s.display()
print()
print("Display:")
print(s.count())