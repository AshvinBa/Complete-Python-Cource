def check_divisibility(n, k):
    
    if 100 <= n <= 999:  
        if n % k == 0:
            print(f"The number is divisible by {k}")
        else:
            print(f"The number is not divisible by {k}")
    else:
        print("Please enter a three-digit number.")

n = int(input("Enter the three-digit number: "))
k = int(input("Enter the value of K: "))

check_divisibility(n, k)
