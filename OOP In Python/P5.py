class Employee:
    company = "Microsoft"
    
    def __init__ (self, name):
        self.name = name
        
    def getDetails(self):
        print(f"Your Name is: {self.name}")
        

ashvin = Employee("Ashvin")

ashvin.getDetails()


    