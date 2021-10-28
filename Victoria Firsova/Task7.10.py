"""Task 7.10. Implement a generator which will generate odd numbers endlessly. Example:

gen = endless_generator()
while True:
    print(next(gen))
>>> 1 3 5 7 ... 128736187263 128736187265 ..."""

def endless_generator():
    num = 0
    while True :
        yield num
        num += 1

gen = endless_generator()
while True:
    print(next(gen))