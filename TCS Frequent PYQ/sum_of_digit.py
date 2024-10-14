# The sum of the digit is divisible by 3.


def sumOfDigit(n):
    sum = 0
    
    while n != 0:
        sum += n%10
        n = n // 10
        
        
    if sum % 3 == 0:
        return 1
    else:
        return 0



n = 123

if sumOfDigit(n):
    print("True.")
else:
    print("False.")
