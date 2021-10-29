"""НЕ ГОТОВОTask 7.7. Implement your custom collection called MyNumberCollection.
It should be able to contain only numbers. It should NOT inherit any other collections.
 If user tries to add a string or any non numerical object there, exception TypeError should be raised.
 Method init sholud be able to take either start,end,step arguments, where start - first number of collection,
  end - last number of collection or some ordered iterable collection (see the example).
   Implement following functionality:

appending new element to the end of collection
concatenating collections together using +
when element is addressed by index(using []), user should get square of the addressed element.
when iterated using cycle for, elements should be given normally
user should be able to print whole collection as if it was list. Example:"""

class MyNumberCollection():
    def __init__(self, start, end=None, step=1):
        self.lst = []
        self.end = end
        self.step = step
        self.start = start

        try:
            if self.end and isinstance(self.end, (int, float)):
                self.end = end
            elif self.end == None:
                pass
            else:
                raise TypeError('MyNumberCollection supports only numbers!')

            if self.step and isinstance(self.step, (int, float)):
                self.step = step
            else:
                raise TypeError ('MyNumberCollection supports only numbers!')

            if self.start and isinstance(self.start, (int, float)) or self.start == 0:
                self.start = start
                for number in range(self.start,self.end,self.step):
                    self.lst.append(number)
                self.lst.append(self.end)
            elif isinstance(self.start, tuple):
                for i in self.start:
                    if isinstance(i,(int,float)):
                        self.lst.append (i)
                    else:
                        raise TypeError ('MyNumberCollection supports only numbers!')

            else:
                raise TypeError ('MyNumberCollection supports only numbers!')
        except TypeError:
            print(f'TypeError:MyNumberCollection supports only numbers!')

    def __next__(self) :
        result = self.lst
        print(result)
        raise StopIteration


    def __iter__(self):
        return self

    def append(self, num):
        try:
            if isinstance(num,(int,float)):
                self.lst.append(num)
            else:
                raise TypeError
        except TypeError:
            print(f'TypeError:{num} is not a number')

    def __add__(self, other):
        if isinstance(other, MyNumberCollection) :
            result = self.lst + other.lst
            return result

    def __getitem__(self, item):
        result = self.lst[item]**2
        return result

    def __repr__(self):
        return f'{self.lst}'


col1 = MyNumberCollection(0, 5, 2)
print(col1)
#[0, 2, 4, 5]
col2 = MyNumberCollection((1,2,3,4,5))
print(col2)
#[1, 2, 3, 4, 5]
col3 = MyNumberCollection((1,2,3,"4",5))
#TypeError: MyNumberCollection supports only numbers!
col1.append(7)
print(col1)
#[0, 2, 4, 5, 7]
col2.append("string")
#TypeError: 'string' - object is not a number!
print(col1 + col2)
# [0, 2, 4, 5, 7, 1, 2, 3, 4, 5]
print(col1)
#[0, 2, 4, 5, 7]
print(col2)
#[1, 2, 3, 4, 5]
print(col2[4])
#>>> 25
for item in col1:
    print(item)
#>>> 0 2 4 5 7