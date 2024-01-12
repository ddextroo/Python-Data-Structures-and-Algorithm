class Node:
    def __init__(self,data):
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
            self.top = self.top.next
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None
        
    def display(self):
        current = self.top
        
        while current:
            print(current.data)
            current = current.next
            
    def reverse(self):
        stack = Stack()
        
        while self.peek():
            stack.push(self.peek())
            self.pop()
        self.top = stack.top
    
    def is_balanced(self, str):
        #loop the string and push each element to the stack
        for i in str:
            #check if the element if it is a symbol like ( { [ ] } )
            if i == '{' or i == '[' or i == '(':
                self.push(i)
            elif self.peek() == '}' or self.peek() == ']' or self.peek() == ')':
                self.pop()
        if self.peek() is None:
            return True
        else:
            return False
    
# initialization
s = Stack()
print(s.is_balanced('[{()}]'))
s.display()