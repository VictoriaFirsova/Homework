"""Task 7.8. Implement your custom iterator class called MySquareIterator which
 gives squares of elements of collection it iterates through. Example:


#>>> 1 4 9 16 25"""


class MySquareIterator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        return self

    def __next__(self):
        result = []

        for num in lst:
            a = num**2
            result.append(a)
        return result


lst = [1, 2, 3, 4, 5]
itr = MySquareIterator(lst)
print(next(itr))

