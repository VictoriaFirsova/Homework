"""Task 7.9. Implement an iterator class EvenRange, which accepts start and end 
of the interval as an init arguments and gives only even numbers during iteration.
 If user tries to iterate after it gave all possible numbers Out of numbers! should be printed.
Note: Do not use function range() at all Example:

er1 = EvenRange(7,11)
next(er1)
>>> 8
next(er1)
>>> 10
next(er1)
>>> "Out of numbers!"
next(er1)
>>> "Out of numbers!"
er2 = EvenRange(3, 14)
for number in er2:
    print(number)
#>>> 4 6 8 10 12 "Out of numbers!"""


class EvenRange:
    def __init__(self, start, end):
        self.start = start
        if self.start % 2 == 0:
            self.start = start
        else:
            self.start = start + 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):

        result = self.start
        if result < self.end:
            self.start += 2

        else:
            result = 'Out of numbers!'

        return result


er1 = EvenRange(7, 11)
print(next(er1))
print(next(er1))
print(next(er1))
print(next(er1))

er2 = EvenRange(3, 14)
for number in er2:
    print(number)