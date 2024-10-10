# Count the number of zeros.

a = (0, 7, 8, 52, 0, 6, 9, 0, 0, 4, 6, 3, 45, 0, 0, 8, 9, 0)
n = len(a)

cnt = 0
for i in range(n):
    if a[i] == 0:  
        cnt += 1

print(f"The number of Zeros are: {cnt}")
