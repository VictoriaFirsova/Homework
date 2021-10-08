"""Task 4.6. Implement a function get_shortest_word(s: str)-> str which returns the longest word in the given string.
The word can contain any symbols except whitespaces ( , \n, \t and so on).
If there are multiple longest words in the string with a same length return the word that occurs first."""


def get_shortest_word(s: str):   # The name of the function in task is not correct for Python
    s = s.split(' ')
    result = []
    for i in s:
        if len(result) != 0:
            if len(i) > len(result[0]):
                result.clear()
                result.append(i)
            else:
                pass
        else:
            result.append(i)
    return result


print(get_shortest_word('Any pythonista like namespaces a lot.'))
