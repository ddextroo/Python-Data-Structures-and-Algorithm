class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Linkedlist:
    def __init__(self):
        self.head = None
    def insert_beginning(self, data):
        
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.head.prev = None
    def display(self):
        current = self.head
        
        while current:
            print(current.data, end="->")
            current = current.next
    def display_reverse(self):
        current = self.head
        while current:
            print(current.prev.data, end="->")
            current = current.next
        
            
    def count_duplicates(self):
        current = self.head
        count = 0

        while current:
            current2 = current.next
            temp_count = 0
            while current2:
                if current.data == current2.data:
                    temp_count += 1
                    if temp_count < 2:
                        count += 1
                    current2.prev.next = current2.next
                    if current2.next:
                        current2.next.prev = current2.prev
                current2 = current2.next
            current = current.next
        return count


    def insert_duplicates(self, l):
        current = l.head
        count = 0
        while current:
            current2 = current.next
            temp_count = 0
            while current2:
                if current.data == current2.data:
                    temp_count += 1
                    if temp_count < 2:
                        count += 1
                    current2.prev.next = current2.next
                    if current2.next:
                        current2.next.prev = current2.prev
                current2 = current2.next
            current = current.next
        
        
                
d = Linkedlist()
d.insert_beginning(2)
d.insert_beginning(1)
d.insert_beginning(7)
d.insert_beginning(10)
d.insert_beginning(10)
d.insert_beginning(10)
d.insert_beginning(9)
d.insert_beginning(7)
d.insert_beginning(1)
d.insert_beginning(6)
d.insert_beginning(10)
d.display()
print()
print(d.count_duplicates())
print()
d2 = Linkedlist()
d2.insert_duplicates(d)
d2.display()