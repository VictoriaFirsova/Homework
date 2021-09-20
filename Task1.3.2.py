# Task 1.3
# Create a program that asks the user for a number and then prints out
# a list of all the [divisors](https://en.wikipedia.org/wiki/Divisor) of that number.
# Examples:
# Input1: 60
# Output1: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}

# num = input('Enter your number: ')
num = 12
num = int(num)
divisors = []
for i in range(num):
    if i == 0:
        continue
    else:
        if num % i == 0:
            divisors.append(i)
divisors.append(num)
print(divisors)
