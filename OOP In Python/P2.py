class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Ashvin Placed in {self.company} and his Salary is {self.salary} .")

        
ashvin = Employee()
ashvin.company = "Microsoft"
ashvin.salary = 1000000000
ashvin.getSalary()
