myList = []

n = int(input("Enter the number of fruits: "))

for i in range(n):
    fruit = input(f"Enter fruit {i+1}: ")
    myList.append(fruit)

print("\nFruits and their indices:")
for index, fruit in enumerate(myList):
    print(f"Index {index}: {fruit}")

