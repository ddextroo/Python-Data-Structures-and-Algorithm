class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def prepend(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            
        current_node.next = new_node
        
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
            print("Linkedlist is empty\n")
            return
        else:
            self.head = current.next
            
    def remove_last(self):
        current = self.head
        
        if self.head is None:
            print("LinkedList is empty\n")
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
            
    def get_length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
     
    def move_given(self, key_from, key_to):
        current = self.head
        
        post_current = current
        pre_current = current
        
        if current is None:
            print("LinkedList is empty\n")
            return
                
        while current.data != key_from:
            pre_current = current
            post_current = current.next.next
            current = current.next
        new_node = Node(key_from)
        pre_current.next = post_current
        while current.data != key_to: 
            post_current = current.next.next
            current = current.next
        current.next = new_node
        new_node.next = post_current
        
        # 37 70 20 40 10
        
    def copy(self, l):
        head_copy = l.head
        while head_copy:
            self.append(head_copy.data)
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
            
    def count_occurrence(self, data):
        current = self.head
        occur = 0
        
        while current:
            print(current.data, "->", data)
            if current.data == data:
                occur += 1
            current = current.next
        return occur
    
    def remove_duplicates(self):
        current = self.head

        while current.next:
            post_current = current.next
            if current.data == post_current.data:
                if post_current.next is None:
                    current.next = None
                    break
                else:
                    current.next = current.next.next
                    break
            current = current.next
        
    def traverse(self):
        new_node = self.head
        
        while (new_node):
            print(new_node.data, end="->")
            new_node = new_node.next
        print()
        print()
            
l = LinkedList()
l.prepend(10)
print("Prepend")
l.traverse()
l.prepend(20)
print("Prepend")
l.traverse()
l.prepend(30)
print("Prepend")
l.traverse()
print("Prepend")
l.traverse()
l.prepend(70)
print("Prepend")
l.traverse()
l.prepend(37)
print("Prepend")
l.traverse()
l.prepend(76)
print("Prepend")
l.traverse()
print("Insert Before given: ") 
l.insert_before_given(30, 50)
l.traverse()
print("Append: ") 
l.append(40)
l.traverse()
print("Insert after given: 50 -> 51") 
l.insert_after_given(50, 51)
l.traverse()
print("Remove first node: 76") 
l.remove_first()
l.traverse()
print("Remove last node: 40") 
l.remove_last()
l.traverse()
print("Remove given node: 20") 
l.remove_given(20)
l.traverse()
print("Update given node: 51 -> 20") 
l.update_given(51, 20)
l.traverse()
print("Update given node: 30 -> 40") 
l.update_given(30, 40)
l.traverse()
print("Move from given node to given node: 70 -> 20") 
l.move_given(50, 20)
l.traverse()
l2 = LinkedList()
l2.copy(l)
l2.append(50)
l2.append(50)
l2.traverse()
l2.reverse()
print()
print(l2.count_occurrence(50))
l2.insert_before_given(50, 50)
l2.traverse()
l2.remove_duplicates()
l2.traverse()

# print("Length:", l.get_length())
