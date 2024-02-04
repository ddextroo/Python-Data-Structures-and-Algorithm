class Node:
    def __init__(self, student_id,major,initial_priority):
        self.student_id = student_id 
        self.major = major 
        self.initial_priority = initial_priority
        self.next = None 
        self.priority = None 

class CollegeAdmission:
    def __init__(self):
        self.front = self.rear = None 
    
    def submit_application(self,student_id,major,initial_priority,priority=None):
        application = Node(student_id, major,initial_priority,priority)
        current = self.front 
        
        if self.is_empty:
            self.front = self.rear= application
        else:
            if self.front.priority is None:
                application.next = self.front
                self.front = application
                return
            if priority is None:
                self.rear.next = application
                self.rear = self.rear.next
                return
            elif priority < self.front.priority:
                application.next = self.front
                self.front = application
                return
            elif self.rear.priority and priority > self.rear.priority:
                self.rear.next = application
                self.rear = self.rear.next
                return
            else:
                while current.next:
                    if current.next.priority is None or priority < current.next.priority:
                        break
                    current = current.next
                application.next = current.next
                current.next = application
    
    def reevaluate_priority(self,student_id,initial_priority):
        current = self.front 
        while current.next:
            if current.student_id == student_id:
                break 
            current = current.next 
            
            
        
                
        
        
    
    def is_empty(self):
        return self.front is None 