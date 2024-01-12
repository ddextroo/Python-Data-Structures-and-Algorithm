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
            if i in "[({":
                self.push(i)
            elif i in "]})":
                if (
                    self.peek()
                    and self.peek() == "("
                    and i == ")"
                    or self.peek() == "["
                    and i == "]"
                    or self.peek() == "{"
                    and i == "}"
                ):
                    self.pop()
                else:
                    return False
        return self.top is None
    def priority(self, str):
        if str in '+-':
            return 1
        elif str in '*/%':
            return 2
        elif str == '^':
            return 3
        elif str in '()':
            return 4
        else:
            return -1
    def remove_whitespace(self, str):
        result = ''
        for i in str:
            if i != ' ':
                result += i
        return result
    def infix_to_postfix(self, str):
        if not self.is_balanced(str):
            return "Expression not balanced"
        str = self.remove_whitespace(str)
        postfix = ''
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
                    while self.peek() and self.priority(i) <= self.priority(self.peek()) and self.peek() != '(':
                        postfix += self.pop()
                    self.push(i)
        while self.peek():
            postfix += self.pop()
        return postfix


s = Stack()
print(s.infix_to_postfix('A+B/C*(D-A)^F^H'))