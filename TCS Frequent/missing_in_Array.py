'''Missing Number in  The Array.'''

def checkMissing(n, lst):
    sum1 = n * (n + 1) // 2  
    sum2 = 0

    for i in range(n - 1):
        sum2 += lst[i]

    diff = sum1 - sum2
    return diff


n = int(input("Enter the size: "))

lst = []  
for i in range(n - 1): 
    value = int(input("Enter the value: "))
    lst.append(value) 
    
print("The missing value is:", checkMissing(n, lst))
