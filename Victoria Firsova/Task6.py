"""Task 4.6. Implement a decorator call_once which runs a function or method once and caches the result.
All consecutive calls to this function should return cached result no matter the arguments."""

result = 0


def call_once(func):
    def wrapper(a, b):
        global result
        if result == 0:
            result = func(a, b)
        return result
    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


print(sum_of_numbers(13, 42))

print(sum_of_numbers(999, 100))

print(sum_of_numbers(134, 412))

print(sum_of_numbers(856, 232))
