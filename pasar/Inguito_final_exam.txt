#Node for jobs
class Node_Job_Posting:
    def __init__(self, title, company_name,description, qualification) -> None:
        self.title = title
        self.company_name = company_name
        self.description = description
        self.qualification = qualification
        self.next = None
#Node for applications
class Node_Application:
    def __init__(self,title,  name, address, status) -> None:
        self.name = name
        self.title = title
        self.status = status
        self.address = address
        self.next = None
#Class Stack for proccess jobs and applications
class Stack:
    #initialize the stack
    def __init__(self) -> None:
        self.top = None
    #jobs posting for employers
    def post_job(self, title, company_name, description, qualification):
        node = Node_Job_Posting(title, company_name, description, qualification)
        if self.top is None:
            self.top = node
            return
        node.next = self.top
        self.top = node
    #function for applying the job
    def apply_for_job(self, title, name, address, status=None):
        node = Node_Application(title, name, address, status)
        
        if self.top is None:
            self.top = node
            return
        node.next = self.top
        self.top = node
    #function for process job applications
    def process_job_application(self):
        if self.top is None:
            return "Applcation is empty"
        removed = self.top.name
        self.top = self.top.next
        return removed
    #function for viewing latest job
    def view_latest_job_posting(self):
        return f"Title: {self.top.title}\nCompany Name: {self.top.company_name}\nDescription: {self.top.description}\nQualifications: {self.top.qualification}" if self.top else None
    #function for viewing latest application
    def view_latest_job_application(self):
        return f"Title: {self.top.title}\nName: {self.top.name}\nAddress: {self.top.address}\nStatus: {self.top.status}" if self.top else None
    #function for close the job opening
    def close_job_opening(self):
        if self.top is None:
            return "Job is empty"
        removed = self.top.title
        self.top = self.top.next
        return removed
    #function for status of applications
    def check_job_appllication_status(self, title):
        current = self.top
        
        #traverse the stack
        while current:
            if current.title == title:
                print(f"Title: {current.title}\nName: {current.name}\nAddress: {current.address}\nStatus: {current.status}\n")
            current = current.next
    def all_job_applications(self):
        current = self.top
        
        #traverse the stack
        while current:
            print(f"Title: {current.title}\nName: {current.name}\nAddress: {current.address}\nStatus: {current.status}\n")
            current = current.next
    #function for displaying all jobs
    def display_jobs(self):
        current = self.top
        
        #traverse the stack
        while current:
            print(f"Title: {current.title}\nCompany Name: {current.company_name}\nDescription: {current.description},\nQualifications: {current.qualification}\n")
            current = current.next
    
jobs = Stack()
applications = Stack()

#job
print("Jobs:")
print()
jobs.post_job("Barista", "Barista Inc", "We are hiring barista", "College Graduate")
jobs.post_job("Dishwasher", "Cafeteria Inc", "We are hiring dishwasher", "High School Graduate")
jobs.post_job("Waiter", "Waiter Inc", "We are hiring Waiter", "Elementary Graduate")
jobs.display_jobs()
print()
print()
print("Latest Job: ")
print()
# jobs.close_job_opening()
print(jobs.view_latest_job_posting())

#applications
applications.apply_for_job("Barista", "Dexter Inguito", "Cebu")
applications.apply_for_job("Dishwasher", "Inguito Dexter", "Mandaue")
print()

print()
#application status
print()
print("Status of specific job:")
print()
print("Barista: ")
print()
applications.check_job_appllication_status("Barista")
print()
# applications.process_job_application()
print("Latest Application: ")
print()
print(applications.view_latest_job_application())
print()
print()
print()
print("All jobs application: ")
print()
applications.all_job_applications()