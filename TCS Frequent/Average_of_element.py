# Find the Average of Element.


def average_of_element(arr,n):
    total_sum=0
    count=0
    
    for i in range(n):
        total_sum+=arr[i]
        count+=1
        
    
    avg = total_sum/count
    print(f"The Average of the Array Element is: {avg}")


n = int(input('Enter the size: '))
arr = []

print("Enter the value: ")

for _ in range(n):
    arr.append(int(input()))
    

average_of_element(arr,n)
