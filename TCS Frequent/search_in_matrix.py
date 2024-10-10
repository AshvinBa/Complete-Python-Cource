# Search in Python.

def search_in_matrix(matrix, n, target):
    i = 0
    j = n - 1
    found = False

    while j >= 0 and i < n:
        if matrix[i][j] == target:
            print(f"{i} {j}")
            found = True
            break
        elif matrix[i][j] > target:
            j -= 1
        else:
            i += 1

    if not found:
        print("No, the target is not available.")


n = int(input("Enter the size: "))
matrix = []

print("Enter the values:")
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

target = int(input("Enter the target: "))
search_in_matrix(matrix, n, target)
