"""Task 4.1. Implement a function which receives a string and replaces all " symbols with ' and vise versa."""


def replacement1(text):      # Если все ковычки в строке одинаковые
    result1 = None
    if text.find("\'") != -1:
        result1 = text.replace("\'", "\"")
    elif text.find("\"") != -1:
        result1 = text.replace("\"", "\'")
    return result1


print(replacement1('I\'m from Russia'))


def replacement2(text):      # Если все ковычки в строке разные
    result2 = str()
    for i in text:
        if i == '\'':
            i = '\"'
            result2 += i
        elif i == '\"':
            i = '\''
            result2 += i
        else:
            result2 += i

    return result2


print(replacement2('I\"m from \'Russia'))
