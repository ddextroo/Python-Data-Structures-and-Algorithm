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
        current = self.head
        new_node = Node(data)
        
        if current is None:
            self.head = new_node
        else:
            while current.next:
                current = current.next   
            current.next = new_node    
    def traverse(self):
        current = self.head
        
        while current:
            print(current.data, end="->")
            current = current.next
    
l = LinkedList()
# l.append(30)
l.prepend(10)
# l.append(20)
# l.append(20)
# l.append(20)
l.prepend(20)
l.traverse()