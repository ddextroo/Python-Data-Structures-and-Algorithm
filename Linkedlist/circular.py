class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = self.tail = None
    
    def insert_first(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = self.tail = new_node
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
            
    def insert_last(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
            
    def insert_before(self, key, data):
        current = self.head
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            self.tail.next = self.head
            return
        if current.data == key:
            self.insert_first(new_node.data)
            return
        while current.data != key:
            pre_current = current
            current = current.next
        pre_current.next = new_node
        new_node.next = current
        
    def insert_after(self,key,data):
        current = self.head
        new_node = Node(data)
        
        if current is None:
            self.head = self.tail = new_node
            self.tail.next = self.head
            return
        if self.tail == key:
            self.insert_after(new_node.data)
            return
        if current.data == key:
            post_current = current.next.next
        while current.data != key:
            post_current = current.next.next
            current = current.next
        current.next = new_node
        new_node.next = post_current
        
        
    def remove_first(self):
        current = self.head
        
        if current is None:
            print("Linkedlist is empty\n")
            return
        self.head = current.next
        self.tail.next = self.head
        
    def remove_last(self):
        current = self.head
        
        if current is None:
            print("Linkedlist is empty\n")
            return
        while True:
            pre_current = current
            current = current.next
            if current.next == self.head:
                break
        self.tail = pre_current
        pre_current.next = self.head
        self.tail.next = self.head
        
    def remove_given(self, data):
        current = self.head
        
        if current is None:
            print("Linkedlist is empty\n")
            return
        if current.data == data:
            self.remove_first()
            return
        if self.tail.data == data:
            self.remove_last()
            return
        while current.data != data:
            pre_current = current
            current = current.next
            if current.next == self.head:
                print("Key not found")
                return
            print()
        pre_current.next = current.next
            
        
    def traverse(self):
        current = self.head
        
        while True:
            print(current.data, end="->")
            current = current.next
            if current == self.head:
                break

    def check(self):
        print("Head: ", self.head.data)
        print("Tail: ", self.tail.data)
        print("Next to tail: ", self.tail.next.data)
c = Linkedlist()

c.insert_first(10)
c.insert_first(20)
c.insert_first(30)
c.insert_first(40)
c.insert_last(45)
c.insert_last(56)
c.traverse()
c.insert_before(40, 15)
print()
c.traverse()
print()
c.insert_after(56, 13)
c.remove_first()
print()
c.traverse()
print()
c.remove_last()
c.traverse()
print()
c.remove_given(30)
print()
c.traverse()
print()
c.check()

print()
# c.remove_first()
# c.traverse()