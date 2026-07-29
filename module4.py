"""
Reads a positive integer N, then N numbers (one by one), then a value X.
Prints the 1-based index of the first occurrence of X among the N numbers,
or -1 if X was not entered.
"""

# Ask the user for N and convert the input string to an integer
n = int(input("Enter N (positive integer): "))

# Create an empty list to store the N numbers
numbers = []

# Loop N times, reading one number per iteration
for i in range(n):
    # Ask for the next number and convert it to an integer
    num = int(input(f"Enter number {i + 1}: "))
    # Add the number to the list
    numbers.append(num)

# Ask the user for X and convert it to an integer
x = int(input("Enter X (integer): "))

# Check whether X appears anywhere in the list
if x in numbers:
    # index() gives the 0-based position of the first match,
    # so add 1 to get the 1-based index required by the assignment
    print(numbers.index(x) + 1)
else:
    # X was not among the N numbers, so print -1
    print(-1)
