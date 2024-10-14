def functionSwap(a,b):
        a = a + b
        b = a - b
        a = a - b
        return a , b
    

a=10
b=20

print("\nBefore Swapping:\n")
print(" a = ",a)
print(" b = ",b)
a,b = functionSwap(a,b)
print(" a = ",a)
print(" b = ",b)