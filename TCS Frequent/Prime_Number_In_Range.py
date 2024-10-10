import math

def check_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solve(a, b):
    ans = []
    for i in range(a, b + 1):
        if check_prime(i):
            ans.append(i)
    return ans

a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))

ans = solve(a, b)

print("The Prime Numbers Between A and B: ", ans)
