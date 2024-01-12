class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None
        

class Stack:
    def __init__(self):
        self.top = None
    
    def push (self,data):
        node = Node(data)
        
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
    
    def pop (self):
        if self.top is None:
            return 'Link is empty'
        else:
            removed_data = self.top.data
            self.top = self.top.next
        return removed_data
    
    def peek(self):
        return self.top.data if self.top is not None else None
    
    def length(self):
        current = self.top
        count = 0
        
        while current:
            count += 1
            current = current.next
        return count
    
    def palindrome(self, str):
        for i in str:
            self.push(i)
            
        for i in str:
            if i == self.peek():
                temp = self.pop()
            else:
                return "Not palindrome"
        return "Palindrome"
    
    def count_duplicates(self):
        current = self.top
        count = 0
        current2 = self.top
        
        while current:
            temp = current
            if temp == current2:
                current2 = current.next
            while current2:
                if current.data == current2.data:
                    count += 1
                current2 = current2.next
            current = current.next 
        return count
    
    def display_reverse(self, str):
        result = ''
        for i in str:
            self.push(i)
        for i in str:
            result += self.pop()
        return result
    
    def search(self, key):
        current = self.top
        
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    
    def merge(self, s):
        stack = s.top
        current = self.top
        
        while current.next:
            self.push(stack.data)
            current = current.next
            stack = stack.next
        
    def reverse(self):
        current = self.top
        self.top = None
        
        while current:
            self.push(current.data)
            current = current.next
            
            
    
    def display(self):
        current = self.top
        
        while current:
            print(current.data,end="")
            current = current.next
    
            
stack = Stack()
# print(stack.palindrome("dexter"))
print()
# print("top", stack.peek())
print()
# stack.display()
print()
# print(stack.display_reverse('dexter'))
print()
stack.push('d')
stack.push('e')
stack.push('x')
stack.push('t')
stack.push('e')
stack.push('r')
stack.display()
print()
stack.reverse()
stack.display()
print()
print()

stack1 = Stack()
stack1.push('b')
stack1.push('i')
stack1.push('x')
stack1.push('y')
stack1.push('o')
stack.merge(stack1)
stack.display()
print()
print(stack.peek())
print()
print(stack.search('o'))