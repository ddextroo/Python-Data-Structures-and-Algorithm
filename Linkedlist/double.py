class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def prepend(self, data):
        current = self.head
        new_node = Node(data)
        
        if current is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def append(self,data):
        current = self.head
        new_node = Node(data)
        
        if current is None:
            self.head = new_node
        else:
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = None
            
    def insert_before(self, key, data):
        current = self.head
        new_node = Node(data)
        
        if current is None:
            print("Linkedlist is empty\n")
            return
        if current.data == key:
            self.prepend(new_node.data)
            return
        while current.data != key:
            current = current.next
        current.prev.next = new_node
        new_node.next = current
        new_node.prev = current.prev
        current.prev = new_node
        
    def insert_after(self, key, data):
        current = self.head
        new_node = Node(data)
        
        if current is None:
            print("Linkedlist is empty\n")
            return
        while current.data != key:
            current = current.next
        post_current = current.next
        current.next = new_node
        new_node.prev = current
        new_node.next = post_current
        post_current.prev = new_node
        
    def delete_first(self):
        current = self.head
        
        if current is None:
            print("Linkedlist is empty")
            return
        self.head = current.next
        current.next.prev = None
        
    def delete_last(self):
        current = self.head
        
        if current is None:
            print("Linkedlist is empty")
            return
        while current.next:
            current = current.next
            
        current.prev.next = None
        
    def delete_given(self, key):
        current = self.head
        
        if current.data == key:
            self.delete_first()
            return
        while current.data != key:
            current = current.next
        if current.next is None:
            self.delete_last()
            return
        post_current = current.next
        current.prev.next = current.next
        post_current.prev = current.prev
       
    def traverse(self):
        current = self.head
        
        while current:
            print("<-",current.prev.data if current.prev is not None else None, "|", current.data, "|", current.next.data if current.next is not None else None, end=" -> \n")
            current = current.next
            
    def reverse(self):
        current = self.head
        self.head = None
        
        while current:
            self.prepend(current.data)
            current = current.next
    
    def concatenate(self, l):
        l_copy = l.head
        
        while l_copy:
            self.prepend(l_copy.data)
            l_copy = l_copy.next
            
    def get_min(self):
        current = self.head
        min = 999999
        while current:
            if current.data < min:
                min = current.data
            current = current.next
        return min
            
    def swap(self, key, data):
        current = self.head
        current2 = self.head
        while current.data != key:
            current = current.next
        temp = current.next
        new_node = Node(current.data)
        self.delete_given(current.data)
        while current2.data != data:
            current2 = current2.next
        if current.next.data == data:
            self.insert_before(current.next.next.data, current.data)
            return
        if current2.next is None:
            self.delete_given(current2.data)
            self.append(current.data)
            self.insert_before(current.next.data, current2.data)
            return
        self.insert_after(current2.data, new_node.data)
        self.delete_given(current2.data)
        self.insert_before(temp.data, current2.data)  
        
    def merge_sorted(self, l1, l2):
        lo = l1.head
        lt = l2.head
        
        while lo:
            self.append(lo.data)
            self.append(lt.data)
            lo = lo.next
            lt = lt.next
            
    def remove_duplicates(self):
        current = self.head

        while current:
            post_current = current.next
            if current.data == current.next.data:
                current.next = current.next.next
                post_current.prev = current
            current = current.next
    def clear(self):
        self.head = None
d = Linkedlist()
d.prepend(10)
d.append(12)
d.prepend(7)
d.append(16)
d.append(14)
d.prepend(21)
d.prepend(24)
d.prepend(23)
d.prepend(25)
d.traverse()
print()
d.insert_before(21, 0)
d.traverse()
print()
print()
d.traverse()
d.insert_after(7,8)
print()
d.traverse()
d.delete_first()
print()
d.traverse()
d.delete_last()
print()
d.traverse()
d.delete_given(10)
print()
d.traverse()
print()
d.traverse()
d2 = Linkedlist()
d2.prepend(2)
d2.prepend(3)
d2.append(10)
d2.prepend(4)
d2.prepend(12)
d2.prepend(9)
print()
print()
print()
d.swap(23,24)
print()
d.traverse()
print()
print()
print()
d.reverse()
d.traverse()
print()
print()
d2.traverse()
d.concatenate(d2)
print()
print()
d.traverse()
print()
print(d.get_min())



# d3 = Linkedlist()
# d4 = Linkedlist()
# d3.append(1)
# d3.append(2)
# d3.append(4)
# d4.append(1)
# d4.append(3)
# d4.append(4)
# d5 = Linkedlist()
# d5.merge_sorted(d3, d4)
# print()
# d5.traverse()
# print()
# d5.remove_duplicates()
# d5.traverse()
# print()
