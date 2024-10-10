def push_into_the_rap(arr, n):
    j = 0

    for i in range(n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1


arr = [0, 0, 1, 2, 4, 5]
n = len(arr)

push_into_the_rap(arr, n)

print("The Distributed Chocolates are:", *arr)
