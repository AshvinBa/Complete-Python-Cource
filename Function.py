#Module function
'''
from math import pow
from math import cos

print(pow(2,2))

print(cos(3.14))
'''

# User Define Function
'''
def greet(name):
    gr="Hello"+name
    return gr

print(greet(" Ashvin"))
'''

# Calling Function.
'''
def greet():
    print("Good Morning Ashvin")
    return

greet()
greet()
greet()
greet()
greet()


def sum_of_marks(number):
    print("Calculating...")
    return sum(number)

sum_list=[1,2,3,4,5,6,7,8,9,10]
sumOfNumber=sum_of_marks(sum_list)
print(sumOfNumber)
'''

# write the function which take the list of the name and say "Hello" to them

def func(name):
    print("Hello ",name)
    return 

list1 = ["Ashvin","Sudhir","Yogita","Gayatri","Nikhil"]
i=0

n=len(list1)

while i<n:
    func(list1[i])
    i+=1














