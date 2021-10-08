"""Task 4.10. Implement a function that takes a number as an argument and returns a
dictionary, where the key is a number and the value is the square of that number."""

# print(generate_squares(5))
# >>> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


def generate_squares(num: int):
    result = {x: x ** 2 for x in range(1, num+1)}

    return result


print(generate_squares(5))
