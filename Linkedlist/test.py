class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Circular:
    def __init__(self):
        self.head = self.tail = None

    def insert_end(self, data):
        node = Node(data)

        if self.head == None:
            self.head = self.tail = node
            self.tail.next = self.head
        else:
            self.tail.next = node
            print()
            print("wow\n", self.tail.data)
            self.tail = node
            print()
            print("wows\n", self.tail.data)
            self.tail.next = self.head

    def display(self):
        current = self.head

        if self.head == None:
            print('\nList is empty')
            return

        while True:
            print(current.data, '', end='')
            current = current.next
            if current == self.head:
                break
        # while current.next != self.head:
        #     print(current.data, '', end='')
        #     current = current.next
        # print(current.data, '', end='')

    def delete_first(self):
        if self.head == None:
            print('\nList is empty')
            return

        self.head = self.head.next
        self.tail.next = self.head

    def check(self):
        print('Head ', self.head.data)
        print('Tail ', self.tail.data)
        print('Next to tail ', self.tail.next.data)


c = Circular()
c.insert_end(5)
c.insert_end(6)
c.insert_end(4)
c.insert_end(9)

print()
c.display()