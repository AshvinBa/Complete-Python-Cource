class Employee:
    company = "Google"
    salary = 100

    # def view(self):
    #     print("Ashvin Placed in Google")


ash = Employee()
raj = Employee()

ash.salary = 300
raj.salary = 500

ash.company = "Microsoft"
raj.company = "Oracle"

print(ash.salary)   
print(raj.salary)   

print(ash.company)  
print(raj.company)  

# ash.view()
