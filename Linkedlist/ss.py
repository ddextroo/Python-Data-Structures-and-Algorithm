class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Singly:
    def __init__(self):
        self.head = None
    def add_beginning(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def display(self):
        current = self.head
        
        while current:
            print(current.data, end="->")
            current = current.next
    def add_last(self,data):
        new_node = Node(data)
        current = self.head
        
        if self.head is None:
            self.head = new_node
            return
        while current.next is not None:
            current = current.next
        current.next = new_node
    def before_given(self,key,data):
        new_node = Node(data)
        current = self.head
        
        if current.data == key:
            new_node.next = self.head
            self.head = new_node
            return
        while current.data != key:
            if current.next is None:
                print('key not found')
                return
            pre_current = current
            current = current.next
        pre_current.next = new_node
        new_node.next = current
    def after_given(self,key,data):
        new_node = Node(data)
        current = self.head
        
        if current.data == key:
            post_current = current.next
            current.next = new_node
            
        
            
            

s = Singly()
s.add_beginning(20)
s.add_beginning(10)
s.add_last(25)
s.display()
    