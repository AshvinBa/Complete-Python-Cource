# Write a program to take a input of X and Y in a new line
# Print the number which is nearer the integer when 
# divided by Y

# Example - 1
# Input: 
# X=13
# Y=3
# Output: 12


def find_nearest(n):
    int_num = int(n)
    dec_num = n - int_num

    if dec_num > 0.5:
        return int_num + 1
    else:
        return int_num



x = int(input("Enter the value of X: "))
y = int(input("Enter the value of Y: "))

nearest = x / y
print("The Nearest Number is:", y * find_nearest(nearest))

