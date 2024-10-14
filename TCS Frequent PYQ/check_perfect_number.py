def CheckPerfectNum(n):
    sum = 0
    for i in range(1 , n // 2 + 1):
        if n % i == 0:
            sum += i         
    return sum == n
    

n=28
a = CheckPerfectNum(n)

if a:
    print("Yes.")
else:
    print("No.")