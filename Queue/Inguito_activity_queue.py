class Node_Stack:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None
class Stack:
    def __init__(self) -> None:
        self.top = None
        
    def push_items(self, item):
        node = Node_Stack(item)
        if self.top is None:
            self.top = node
            return
        node.next = self.top
        self.top = node
    def display(self):
        current = self.top
        while current:
            print(current.item)
            current = current.next
    def count(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count

class Node:
    def __init__(self, items, order_ID, timestamp) -> None:
        self.order_ID = order_ID
        self.items = items
        self.timestamp = timestamp
        self.next = None

class Order:
    def __init__(self) -> None:
        self.front = self.rear = None

    def enqueue(self, items, order_ID, timestamp):
        node = Node(order_ID, items, timestamp)
        if self.front is None or self.rear is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dispatch_front(self):
        if self.front is None:
            return "Empty"
        removed = self.front.order_ID
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        return removed

    def dispatch_rear(self):
        if self.rear is None:
            return "Empty"
        current = self.front
        while current.next:
            pre_current = current
            current = current.next
        pre_current.next = None
        self.rear = pre_current
    def move_late(self):
        current = self.front
        # self.front = None
        while current:
            node = Node(current.items, current.order_ID, current.timestamp)
            if self.front is None and self.rear is None:
                self.front = self.rear = node
            if current.timestamp or self.rear.timestamp and current.timestamp > self.rear.timestamp:
                self.rear.next = node
                self.rear = node
                return
            if self.front.timestamp or self.front.timestamp and current.timestamp > self.front.timestamp:
                node.next = self.front
                self.front = node
                return
            current2 = self.front
            while current2.next:
                if current2.next.timestamp or current.timestamp <= current2.next.timestamp:
                    break
                current2 = current2.next
            temp = current2.next
            current2.next = node
            node.next = temp
            current = current.next
    def order_queue(self):
        current = self.front
        while current:
            print(current.order_ID, end="->")
            items = current.items.top
            while items:
                print(items.item, end="|")
                items = items.next
            print(current.timestamp)
            print()
            current = current.next
    def delivery_time(self, order_ID):
        current = self.front
        
        while current.order_ID != order_ID:
            current = current.next
        items = current.items.top
        time = 0
        while items:
            time += 3600
            items = items.next
        return time
        

s = Stack()
s2 = Stack()
s.push_items("Bag")
s.push_items("Shoes")
s.push_items("Pants")
s2.push_items("Food")
s2.push_items("food2")
s2.push_items("food3")
o = Order()
o.enqueue(2612, s2, 15612)
o.enqueue(1527, s, 15731)
o.order_queue()
print("Delivery Time: ", o.delivery_time(1527))
# o.move_late()
o.order_queue()
