"""Task 4.7. Implement a function foo(List[int]) -> List[int] which, given a list of integers,
return a new list such that each element at index i of the new list is the product of
all the numbers in the original array except the one at i."""


def foo(list_of_integers: list[int]):
    result_l = []
    for i in list_of_integers:
        result = 1
        for a in list_of_integers:
            if a == i:
                continue
            else:
                result *= a
        result_l.append(result)
    return result_l


print(foo([1, 2, 3, 4, 5]))
print(foo([3, 2, 1]))
