class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_beginning(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
    def add_last(self, data): # 3
        new_node = Node(data)
        current = self.head
        
        if self.head is None:
            self.head = new_node
            return
        while current.next is not None:
            current = current.next
        current.next = new_node
            
    def traverse(self):
        current = self.head
        
        while current:
            print(current.data, end="->")
            current = current.next
            
    def insert_before_given(self, key, data):
        new_node = Node(data)
        current = self.head
        
        if current.data == key:
            new_node.next = self.head
            self.head = new_node
            return
        while current.data != key:
            if current.next is None:
                print("Key not found")
                return
            pre_current = current
            current = current.next
        pre_current.next = new_node
        new_node.next = current
    
    def insert_after_given(self, key, data):
        new_node = Node(data)
        current = self.head
        
        if current.data == key:
            post_current = current.next
            current.next = new_node
            new_node.next = post_current
            return
        post_current = current.next
        while current.data != key:
            if current.next is None:
                print("Key not found")
                return
            post_current = current.next.next
            current = current.next
        current.next = new_node
        new_node.next = post_current
        
    def remove_first(self):
        current = self.head
        
        if self.head is None:
            return
        else:
            self.head = current.next
            
    def remove_last(self):
        current = self.head
        
        if self.head is None:
            return
        else:
            while current.next:
                pre_current = current
                current = current.next
            pre_current.next = None
            
    def remove_given(self, key): 
        current = self.head
        
        if current is None:
            print("Linkedlist is empty\n")
            return
        else:
            if current.data == key:
                self.head = current.next
            else:
                post_current = current.next
                while current.next.data != key:
                    if post_current.next is None:
                        print("Key not found")
                        return
                    post_current = current.next.next
                    current = current.next
                current.next = post_current.next
                
    def update_given(self, key, data):
        new_node = Node(data)
        current = self.head
        
        if current is None:
            print("Linkedlist is empty\n")
            return
        else:
            if current.data == key:
                new_node.next = self.head
                self.head = new_node
                post_current = self.head.next.next
                self.head.next = post_current
                return
            post_current = current.next
            while current.next.data != key:
                post_current = current.next.next
                if post_current is None:
                    print("Key not found")
                    return
                current = current.next
            current.next = new_node
            new_node.next = post_current.next
            
    def move_given_to_after(self, key_from, key_to):
        current = self.head
        
        post_current = current
        pre_current = current
        
        if current is None:
            print("LinkedList is empty\n")
            return
        while current.data != key_from:
            pre_current = current
            post_current = current.next.next
            if post_current is None:
                print("Key from not found")
                return
            current = current.next
        new_node = Node(key_from)
        pre_current.next = post_current
        while current.data != key_to: 
            if current.next is None:
                print("Key to not found")
                return
            post_current = current.next.next
            current = current.next
        current.next = new_node
        new_node.next = post_current
        
    def count(self):
        current = self.head
        
        count = 0
        while current is not None:            
            count += 1
            current = current.next
        return count
    
    def copy(self, l):
        head_copy = l.head
        while head_copy:
            self.add_last(head_copy.data)
            head_copy = head_copy.next
        
    def reverse(self):
        current = self.head
        pre_current = None
        
        while current:
            post_current = current.next 
            current.next = pre_current 
            pre_current = current
            current = post_current
                
        while pre_current:
            print(pre_current.data, end="->")
            pre_current = pre_current.next
            
    def count_occurrence(self, key, data):
        current = self.head
        count = 0
        
        while current:
            if current.data == key:
                count += 1
            current = current.next

l = LinkedList()
l.add_beginning(22)
l.add_beginning(2)
l.add_beginning(3)
l.add_beginning(4)
l.add_last(7)
l.add_last(8)
print("Trav")
print()
l.traverse()
print()
print("Rev")
print()
l.reverse()
print()
print("Trav")
print()
l.traverse()
print()
print(l.count())
l2 = LinkedList()
print()
l2.copy(l)
l2.traverse()
l2.copy(l)
print()
print("Gwapo dexter")
l2.traverse()
print()
            
            
            
            
        