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
            if i in "({[":
                self.push(i)
            elif i in ")]}":
                if (
                    self.peek()
                    and self.peek() == "("
                    and i == ")"
                    or self.peek() == "{"
                    and i == "}"
                    or self.peek() == "["
                    and i == "]"
                ):
                    self.pop()
                else:
                    return False
        return self.peek() is None

    def remove_whitespace(self, str):
        result = ""
        for i in str[::-1]:
            if i not in " ":
                self.push(i)
        while self.peek():
            result += self.pop()
        return result

    def priority(self, operator):
        if operator in "+-":
            return 1
        elif operator in "*/%":
            return 2
        elif operator == "^":
            return 3
        elif operator in "()":
            return 4
        else:
            return -1

    def calculate(self, operand1, operator, operand2):
        if operator == "+":
            return operand1 + operand2
        elif operator == "-":
            return operand1 - operand2
        elif operator == "*":
            return operand1 * operand2
        elif operator == "/":
            return operand1 / operand2
        elif operator == "%":
            return operand1 % operand2
        elif operator == "^":
            return operand1 ^ operand2

    def infix_to_postfix(self, str):
        if not self.is_balanced(str):
            return "Expression not balanced"

        str = self.remove_whitespace(str)
        postfix = ""
        for i in str:
            if self.priority(i) < 0:
                postfix += i
            else:
                if i == "(":
                    self.push(i)
                elif i == ")":
                    while self.peek() != "(":
                        postfix += self.pop()
                    self.pop()
                else:
                    while (
                        self.peek()
                        and self.priority(i) <= self.priority(self.peek())
                        and self.peek() != "("
                    ):
                        postfix += self.pop()
                    self.push(i)
        while self.peek():
            postfix += self.pop()
        return postfix

    def infix_to_prefix(self, str):
        if not self.is_balanced(str):
            return "Expression not balanced"

        str = self.remove_whitespace(str)
        prefix = ""
        for i in str[::-1]:
            if i == ")":
                prefix += "("
            elif i == "(":
                prefix += ")"
            else:
                prefix += i
        final_prefix = ""
        for i in prefix:
            if self.priority(i) < 0:
                final_prefix += i
            else:
                if i == "(":
                    self.push(i)
                elif i == ")":
                    while self.peek() != "(":
                        final_prefix += self.pop()
                    self.pop()
                else:
                    while (
                        self.peek()
                        and self.priority(i) < self.priority(self.peek())
                        and self.peek() != "("
                    ):
                        final_prefix += self.pop()
                    self.push(i)
        while self.peek():
            final_prefix += self.pop()
        return final_prefix[::-1]

    def evaluate_postfix(self, str):
        temp = ''
        for i in str:
            if self.priority(i) < 0 or i == ' ':
                if not i == ' ':
                    self.push(temp)
                    temp = ''
                temp += i
            elif self.priority(i) > 0:
                num1 = self.pop()
                num2 = self.pop()
                answer = self.calculate(int(num2), i, int(num1))
                self.push(answer)
        return self.peek()
    def evaluate_prefix(self, str):
        for i in str[::-1]:
            if self.priority(i) <    0:
                self.push(i)
            else:
                num1 = self.pop()
                num2 = self.pop()
                answer = self.calculate(int(num2), i, int(num1))
                self.push(answer)
        return self.peek()


s = Stack()
expression = "A*B-C(E+F/G-)"
print(s.infix_to_postfix(expression))
print(s.infix_to_prefix(expression))
print()
#evaluate = '22+3*10-'
#print(s.evaluate_postfix(evaluate))
# print(s.evaluate_prefix(evaluate))
