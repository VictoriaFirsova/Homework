"""Task 7.5. Implement function for check that number is even and is greater than 2.
Throw different exceptions for this errors. Custom exceptions must be derived from custom base exception
(not Base Exception class)."""


def check_number(num):
    result = None
    try:
        num = int(num)
        if num % 2 == 0 and num > 2:
            result = "Number is even and is greater than 2"
        else:
            result = "Number is not even and is greater than 2"
    except ValueError:
        print("It's not an int")

    return result


print(check_number(3))
print(check_number(6))
check_number('f')
