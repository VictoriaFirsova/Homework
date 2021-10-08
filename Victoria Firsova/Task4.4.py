"""Task 4.4. Implement a function split_by_index(s: str, indexes: List[int]) ->
List[str] which splits the s string by indexes specified in indexes. Wrong indexes must be ignored."""


def split_by_index(s: str, indexes: list[int]):
    result_list = []
    count = 0
    for i in indexes:
        if i <= len(s):
            try:
                if count == 0:
                    result_list.append(s[:i])
                    count = i
                else:
                    result_list.append(s[count:i])
                    count = i
            except IndexError as error:
                pass
    result_list.append(s[count:])
    return result_list


print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
print(split_by_index("no luck", [42]))
