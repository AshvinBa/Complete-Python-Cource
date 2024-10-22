# Static Method.

class Employee:
    company = "Google"
    
    def getSalary(self, signature):
        print(f"Salary for the Employee working in {self.company} is {self.salary}\n{signature}")
    
    @staticmethod
    def greet():
        print("Good Morning, sir.")
        

ash = Employee()
ash.company = "TCS"
ash.salary = 50000  # Define the salary attribute
ash.getSalary("Thanks")
ash.greet()
