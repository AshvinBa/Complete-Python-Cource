# Calculator Project

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

while True:
    print('\n\n*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*')
    print("\tCalculator")
    print("\t1) Addition")
    print("\t2) Subtraction")
    print("\t3) Multiplication")
    print("\t4) Division")
    print("\t5) Exit")
    
    choice = int(input("\tEnter your choice: "))
    
    if choice == 5:
        print("\tExit.")
        break
    elif choice in [1, 2, 3, 4]:
            a = int(input("\tEnter A: "))
            b = int(input("\tEnter B: "))
        
    if choice == 1:
            print("\tAddition: ", add(a, b))
    elif choice == 2:
            print("\tSubtraction: ", sub(a, b))
    elif choice == 3:
            print("\tMultiplication: ", mul(a, b))
    elif choice == 4:
            print("\tDivision: ", div(a, b))
    else:
        print("\tInvalid choice. Please choose a number between 1 and 5.")














































































