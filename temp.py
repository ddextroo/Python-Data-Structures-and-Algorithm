#qstackdqdjwdiwf
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
class Stack:
    def __init__(self) -> None:
        self.top = None
    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
            return
        node.next = self.top
        self.top = node
    def pop(self):
        if self.top is None:
            return "Is empty"
        removed = self.top.data
        self.top = self.top.next
        return removed
    def peek(self):
        return self.top.data if self.top else None
    def display(self):
        current = self.top
        
        while current:
            print(current.data)
            current = current.next
    def palindrome(self, str):
        for i in str:
            self.push(i)
            
        for i in str:
            print(self.peek(), i)
            if self.peek() == i:
                self.pop()
            else:
                return False
        return self.top is None
    def reverse(self, str):
        temp = Stack()
        for i in str:
            temp.push(i)
        rev = ''
        while temp.peek():
            rev += temp.pop()
        return rev
    def copy(self, s):
        temp = Stack()
        while s.peek():
            temp.push(s.pop())
        while temp.peek():
            self.push(temp.pop())
s = Stack()
s.display()
s.push(2)
s.push(1)
s.push(6)
s.push(4)
print()
print()
s.display()
print()
print()
print()
s2 = Stack()
s2.copy(s)
s2.display()
#test
