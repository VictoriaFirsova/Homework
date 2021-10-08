"""Task 4.2. Write a function that check whether a string is a palindrome or not. Usage of any reversing functions is
prohibited. To check your implementation you can use strings from here. """


def palindrome(text):
    reversed_string = text[::-1]
    if text == reversed_string:
        result = 'String is a palindrome'
    else:
        result = 'String is not a palindrome'
    return result


print(palindrome('reviver'))
