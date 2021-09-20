# Task 1.6
# Write a Python program to convert a given tuple of positive integers into an integer.
# Examples:
# Input: (1, 2, 3, 4)
# Output: 1234

given_tuple = (1, 66, 3, 9)
result_integer = []
for integer in given_tuple:
    result_integer.append(str(integer))
result_integer = ''.join(result_integer)
print(result_integer)
