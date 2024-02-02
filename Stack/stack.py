class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class stack:
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
            removed = None
        else:
            removed = self.top.data
            self.top = self.top.next

        return removed
#fgodwqqss
    def peek(self):
        return self.top.data if self.top else None


    def traverse(self):
        current = self.top

        while current:
            print(current.data, end="->")
            current = current.next
        print()
    # def is_palindrome(self, str):
    #     for i in str:
    #         self.push(i)
    #     for i in  str:
    #         if i == self.peek():
    #             temp = self.pop()
    #         else:
    #             return "Not palindrome"
    #     return "Palindrome"
    
    def is_palindrome(self,str):
        for i in str:
            self.push(i)
        
        for i in str:
            if i == self.peek():
                temp = self.pop()
        return True if self.peek() is None else False
    
    def display_reverse(self):
        temp = stack()
        result = ''
        
        while self.peek():
            temp.push(self.pop())
        self.top = temp.top
        
        while temp.peek():
            # print(temp.peek)
            result += temp.pop()
            
        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
    def parenthesis(self, str):
        for i in str:
            self.push(i)
        for i in str:
            if i == '(':
                if self.peek() != ')':
                    return False
            if i == '{':
                if self.peek() != '}':
                    return False
            if i == '[':
                if self.peek() != ']':
                    return False
            temp = self.pop()
        return True
    def getMin(self):
        min = 99999
        current = self.top
        
        while current:
            if int(current.data) < min:
                min = int(current.data)
            current = current.next
            
        return min
s = stack()

print()

print()
print()
print(s.is_palindrome('9835412'))
print("top:", s.peek())
print()
# s.traverse()
expr = '()'
print(s.parenthesis(expr))
# print(s.display_reverse("rawr"))
s.traverse()
print(s.getMin())
print(s.display_reverse())
