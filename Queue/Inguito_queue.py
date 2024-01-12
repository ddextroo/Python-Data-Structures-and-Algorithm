class Node:
    # initialization of node to submit application
    def __init__(self, student_id, major, initial_priority) -> None:
        self.student_id = student_id
        self.major = major
        self.initial_priority = initial_priority
        self.next = None


# class on college submission
class CollegeAdmission:
    # initialization of front and rear
    def __init__(self) -> None:
        self.front = self.rear = None

    # function to submit the application based on initial_priority
    def submit_application(self, student_id, major, initial_priority=None):
        node = Node(student_id, major, initial_priority)
        # if theres none, just add
        if self.front is None and self.rear is None:
            self.front = self.rear = node
            return
        # insert at the end if high
        if initial_priority is None or self.rear.initial_priority and initial_priority > self.rear.initial_priority:
            self.rear.next = node
            self.rear = node
            return
        # insert at the beginning if low
        if (
            self.front.initial_priority is None
            or self.front.initial_priority
            and initial_priority < self.front.initial_priority
        ):
            node.next = self.front
            self.front = node
            return
        #traverse the list if it is less than then insert the node based on the initial_priority
        current = self.front
        while current.next:
            if current.next.initial_priority is None or initial_priority <= current.next.initial_priority:
                break
            current = current.next
        temp = current.next
        current.next = node
        node.next = temp
        if current.next.next and current.next.initial_priority == current.next.next.initial_priority:
            self.rear = node
        return

    # function to display the students info
    def display(self):
        current = self.front
        while current:
            print("Student ID: ",current.student_id, "\tInitial_priority: ", current.initial_priority)
            current = current.next

    # function to admit and remove
    def admit_student(self):
        if self.front is None:
            return None
        remove = self.front.student_id
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return remove

    # function to reevaluate property
    def reevaluate_initial_priority(self, student_id, initial_priority=None):
        current = self.front
        while current.student_id != student_id:
            pre_current = current
            current = current.next
        node = Node(current.student_id, current.major, initial_priority)
        pre_current.next = current.next
        pre_current.next = node
        node.next = current.next

    # get the list of applications
    def get_application_count(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count


# initialization
c = CollegeAdmission()
c.submit_application("12345", "BSIT", 5)
c.submit_application("12721", "BSIS", 1)
c.submit_application("12612", "BSMT", 10)
c.submit_application("123543", "BSED", 11)
# reevaluate initial priority
c.submit_application("12377", "BSAMP")
c.reevaluate_initial_priority("12377",13)
c.submit_application("12612", "BSMT", 5)
c.submit_application("123543", "BSED", 2)
c.display()
# admin student
print("Student: ", c.admit_student())
# c.display()
print()
print()

print()
print()
print()
c.display()
print("Total Application", c.get_application_count())
