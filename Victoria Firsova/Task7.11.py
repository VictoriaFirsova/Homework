"""Task 7.11. Implement a generator which will geterate Fibonacci numbers endlessly. Example:

gen = endless_fib_generator()
while True:
    print(next(gen))
>>> 1 1 2 3 5 8 13 ..."""

def endless_fib_generator():
    num = 1
    first_num = 0
    second_num = 1
    while True:
        yield num
        num = first_num + second_num
        first_num = second_num
        second_num = num

gen = endless_fib_generator()
while True:
    print(next(gen))