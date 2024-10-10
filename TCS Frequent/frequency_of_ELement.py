# Count the Frequency of the element.

def count_frequency_of_element(arr, n):
    
    frequency_map = {}
    
    for i in range(n):
        if arr[i] in frequency_map:
            frequency_map[arr[i]] += 1
        else:
            frequency_map[arr[i]] = 1

    for element, count in frequency_map.items():
        # if count > 1:
            print(element, count)


def frequencyOfElement(arr,n):
    
    for i in range(n):
        cnt=0
        for j in range(n):
            if arr[i] == arr[j]:
                cnt+=1
        print(f"\n{arr[i]} is found at {cnt} times.")

arr = [1, 2, 2, 3, 4, 5, 5, 5]
n = len(arr)
count_frequency_of_element(arr, n)
frequencyOfElement(arr,n)    
    