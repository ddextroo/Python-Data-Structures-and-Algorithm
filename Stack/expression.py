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
            
    def is_empty(self):
        return True if self.top is None else False
    
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
    def remove_whitespace(self, str):
        result = ''
        for i in str:
            if i not in ' ':
                self.push(i)
        while self.peek():
            result += self.pop()
        return result[::-1]             
    def priority(self, char):
        if char in '+-':
            return 1
        elif char in '*/%': 
            return 2
        elif char == '^':
            return 3
        elif char in '()':
            return 4
        else:
            return -1  
    def calculate(self, operand1, operator, operand2):
        if operator in '+':
            return operand1 + operand2
        elif operator in '-':
            return operand1 - operand2
        elif operator in '*':
            return operand1 * operand2
        elif operator in '/':
            return operand1 / operand2
        elif operator in '%':
            return operand1 % operand2
        elif operator in '^':
            return operand1 ^ operand2 
    def infix_to_postfix(self, str):
        if self.is_balanced(str):
            postfix = ''
            str = self.remove_whitespace(str)
            for i in str:
                if self.priority(i) < 0:
                    postfix += i
                else:
                    if i == '(':
                        self.push(i)
                    elif i == ')':
                        while self.peek() != '(':
                            postfix += self.pop()
                        self.pop()
                    else:
                        while not self.is_empty() and self.priority(i) <= self.priority(self.peek()) and self.peek() != '(':
                            postfix += self.pop()
                        self.push(i)
                    
            while not self.is_empty():
                postfix += self.pop()
            return postfix
        else:
            return "Expression not balanced"
    def infix_to_prefix(self, str):
        if self.is_balanced(str):
            str = self.remove_whitespace(str)
            prefix = ''
            for i in str:
                if i == '(':
                    self.push(')')
                elif i == ')':
                    self.push('(')
                else:
                    self.push(i)
            while self.peek():
                prefix += self.pop()        
            postfix = ''
            for i in prefix:
                if self.priority(i) < 0:
                    postfix += i
                else:
                    if i == '(':
                        self.push(i)
                    elif i == ')':
                        while self.peek() != '(':
                            postfix += self.pop()
                        self.pop()
                    else:
                        while not self.is_empty() and self.priority(i) < self.priority(self.peek()) and self.peek() != '(':
                            postfix += self.pop()
                        self.push(i)
                    
            while not self.is_empty():
                postfix += self.pop()
            
            for i in postfix:
                self.push(i)
            result = ''
            while self.peek():
                result += self.pop()
            return result
        else:
            return "Expression is not balanced"
    def prefix_to_postfix(self, str):
        self.top = None
        result = ''
        for i in str:
            self.push(i)
        while self.peek():
            result += self.pop()
        for i in result:
            if self.priority(i) < 0:
                self.push(i)
            elif not self.is_empty():
                temp = self.pop() + self.pop() + i
                self.push(temp)
        final = ''
        while self.peek():
            final += self.pop()
        return final
    def postfix_to_prefix(self, str):
        self.top = None
        result = ''
        for i in str:
            if self.priority(i) < 0:
                self.push(i)
            elif not self.is_empty():
                temp = self.pop() + self.pop() + i
                self.push(temp)
        return self.peek()[::-1]
    def evaluate_postfix(self, expression):
        
        for i in expression:
            if self.priority(i) < 0:
                self.push(i)
            else:
                num1 = self.pop()
                num2 = self.pop()
                answer = self.calculate(int(num2), i, int(num1))
                self.push(answer)
        return self.peek()
    def evaluate_prefix(self, expression):
        answer = ''
        for i in expression:
            self.push(i)
        while self.peek():
            answer += self.pop()
        return self.evaluate_postfix(answer)
    def prefix_to_infix(self, str):
        result = ''
        for i in str:
            self.push(i)
        while self.peek():
            result += self.pop()
        for i in result:
            if self.priority(i) < 0:
                self.push(i)
            else:
                combine = '(' + self.pop() + i + self.pop() + ')'
                self.push(combine)
        final = ''
        while self.peek():
            final += self.pop()
        return final
    def postfix_to_infix(self, str):    
        for i in str:   
            if self.priority(i) < 0:
                self.push(i)
            else:
                combine = ')' + self.pop() + i + self.pop() + '('
                self.push(combine)
        final = ''
        while self.peek():
            final += self.pop()
        return final[::-1]
    
s = Stack()
print(s.infix_to_postfix("(A + B + C + D)"))
print(s.infix_to_prefix("A * B + C / D"))
