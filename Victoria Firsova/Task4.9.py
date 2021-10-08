"""Task 4.9
Implement a bunch of functions which receive a changeable number of strings and return next parameters:
characters that appear in all strings
characters that appear in at least one string
characters that appear at least in two strings
characters of alphabet, that were not used in any string
Note: use string.ascii_lowercase for list of alphabet letters
"""
import string

test_strings = ["hello", "world", "python", ]


def test_1_1(*strings):  # characters that appear in all strings
    result = []
    for string in strings:
        word = string[0]
        for i in word:
            result.append(i)
    result = set(result)
    result = list(result)
    for word2 in string[1:]:

        for letter in result[:]:
            if letter in word2:
                continue
            else:
                if letter in result:
                    result.remove(letter)
                else:
                    continue

    return result


print(test_1_1(["hello", "world", "python", ]))


def test_1_2(*strings):  # characters that appear in at least one string
    result = []
    for string in strings:
        for word in string:
            for i in word:
                result.append(i)
    result.sort()
    result = set(result)
    return result


print(test_1_2(["hello", "world", "python", ]))


def test_1_3(*strings):  # characters that appear at least in two strings
    result = []
    for string in strings:
        word = string[0]
        for i in word:
            result.append(i)
    result = set(result)
    result = list(result)
    for letter in result[:]:
        count = 1
        for word2 in string[1:]:
            if letter in word2:
                count += 1
        if count < 2:
            result.remove(letter)

    return result


print(test_1_3(["hello", "world", "python", ]))


alphabet = string.ascii_lowercase


def test_1_4(*strings):  # characters of alphabet, that were not used in any string
    used_letters = []
    result = []
    for string in strings:
        for word in string:
            for i in word:
                used_letters.append(i)
    used_letters.sort()
    used_letters = set(used_letters)
    used_letters = list(used_letters)
    for letter in alphabet:
        if letter not in used_letters:
            result.append(letter)
    return result


print(test_1_4(["hello", "world", "python", ]))
