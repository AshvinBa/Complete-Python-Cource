def check_armstrong(n):
    temp = n
    cnt = 0
    original = n

    while n != 0:
        cnt += 1
        n = n // 10  

    
    num = 0
    while temp != 0:
        digit = temp % 10
        num += digit ** cnt  
        temp = temp // 10

    return num == original

# Input from the user
n = int(input("Enter the number: "))

# Check if the number is Armstrong
if check_armstrong(n):
    print("Yes, the number is Armstrong.")
else:
    print("No, the number is not Armstrong.")



