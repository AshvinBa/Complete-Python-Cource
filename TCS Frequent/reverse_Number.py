num = int(input("Enter the digit: "))

temp = num
number = 0

while temp != 0:
    digit = temp % 10  
    number = number * 10 + digit  
    temp = temp // 10  

print("Reversed Number:", number)
