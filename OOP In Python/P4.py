class Employee:
    company = "Google"
    
    def __init__(self, name, salary, subunit):  # Corrected to double underscores
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is Created!")
        
    def getDetail(self):
        print(f"The Name of the Employee is: {self.name}")
        print(f"The Salary of the Employee is: {self.salary}")
        print(f"The Subunit of the Employee is: {self.subunit}")
        
    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary} \n{signature}")
        
    @staticmethod
    def greet():
        print("Good Morning, Sir")
    
    @staticmethod
    def time():
        print("The Time is 9 AM in the Morning.")
        
        
ashvin = Employee("Ashvin", 500000, "YouTube")
ashvin.getDetail()