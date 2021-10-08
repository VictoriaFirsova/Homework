"""Task 4.5. Implement a function get_digits(num: int) -> Tuple[int] which returns a tuple
of a given integer's digits."""


def get_digits(num: int):
    result_tuple = []
    num = str(num)
    for i in num:
        i = int(i)
        result_tuple.append(i)
    result_tuple = tuple(result_tuple)
    return result_tuple


print(get_digits(87178291199))
