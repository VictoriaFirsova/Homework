"""Task 4.8. Implement a function get_pairs(lst: List) -> List[Tuple]
which returns a list of tuples containing pairs of elements.
Pairs should be formed as in the example. If there is only one element in the list return None instead."""


def get_pairs(lst: list):
    result = []
    if len(lst) > 1:
        for i in lst:
            next_num = lst.index(i)+1
            if next_num <= len(lst)-1:
                pre_result = [i, lst[next_num]]
                result.append(pre_result)
        result = tuple(result)
    else:
        result = None

    return result


print(get_pairs([1, 2, 3, 8, 9]))
print(get_pairs(['need', 'to', 'sleep', 'more']))
print(get_pairs([1]))
