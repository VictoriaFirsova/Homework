# Task 1.3
# Write a Python program that accepts a comma separated sequence of words as input and prints the
# unique words in sorted form.
# Examples:
# Input4: ['red', 'white', 'black', 'red', 'green', 'black']
# Output4: ['black', 'green', 'red', 'white', 'red']

my_list = ['red', 'white', 'black', 'red', 'green', 'black']
result_list = set(my_list)
result_list = list(result_list)
result_list = sorted(result_list)

print(result_list)