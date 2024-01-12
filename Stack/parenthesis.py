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
        return self.top.data if self.top else None
        
    def display(self):
        current = self.top
        
        while current:
            print(current.data, end="")
            current = current.next
        
    
    def is_balanced(self, str):
        for i in str:
            if i in '([{':
                self.push(i)
            elif i in ')}]':
                print(i, self.peek())
                if self.peek() and self.peek() == '(' and i == ')' or self.peek() == '[' and i == ']' or self.peek() == '{' and i == '}':
                    self.pop()
                else:
                    return False
        return self.peek() is None
s = Stack()
print(s.is_balanced('A+B*(C+D-E*F))+G'))
s.display()
