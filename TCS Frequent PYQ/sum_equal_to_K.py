
# Check Wheather that the pair of i<j , num[i]-num[j]==k.

# Input : 1 2 2 1
# Output : 4


def build_frequency_map(arr):
    frequency = {}
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1
    return frequency

def count_pair_with_difference(arr, k, frequency):
    count = 0
    for num in arr:
        if (num + k) in frequency:
            count += frequency[num + k]  
    return count

if __name__ == "__main__":
    input_str = input("Enter the values: ")
    arr = list(map(int, input_str.split()))
    
    k = arr[-1]
    arr.pop()

    frequency = build_frequency_map(arr)
    result = count_pair_with_difference(arr, k, frequency)

    print("The sum of the Number is:", result)
