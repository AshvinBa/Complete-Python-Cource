# I/P: 
# arr = [0 1 0 1 1 1 0]
# O/P:  [0 0 0 1 1 1 1]


def separet(arr,n):
    low=0
    for i in range(n):
        if arr[i]==0:
            arr[i] , arr[low] = arr[low] , arr[i]
            low+=1


arr =[0,1,0,0,1,1]
n = len(arr)
separet(arr,n)

for ele in arr:
    print(ele,end=" ")