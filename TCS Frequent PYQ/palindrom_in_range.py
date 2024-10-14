# Questions- 
# Find the all palindrom number between range.
# Input:
# A=100 B=150
# Output: [101,111]

# Input:
# A=11 B=20
# Output: [11]


def check_palindrome(number):
    temp = number  
    reversed_num = 0  

    while number != 0:
        remainder = number % 10
        reversed_num = reversed_num * 10 + remainder
        number = number // 10

    return temp == reversed_num

def find_palindromes_in_range(a, b):
    palindromes = []

    for i in range(a, b + 1):
        if check_palindrome(i):
            palindromes.append(i)

    return palindromes

if __name__ == "__main__":
    a = int(input("Enter the value of A: "))
    b = int(input("Enter the value of B: "))

    palindromic_numbers = find_palindromes_in_range(a, b)
    print("The palindrome numbers array is:", palindromic_numbers)
