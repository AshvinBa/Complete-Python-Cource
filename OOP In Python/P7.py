# Finding the Square , Cube and SquareRoot.

class Calculator:
    def __init__ (self,num):
        self.num = num
        
    def square(self):
        print(f"The Square of the Number is: {self.num**2}")
    
    def squareRoot(self):
        print(f"The value of SquareRoot is: {self.num**0.5}")
    
    def cube(self):
        print(f"The Cube of the Number is: {self.num**3}")
        

Ashvin = Calculator(3)
Ashvin.square()
Ashvin.squareRoot()
Ashvin.cube()