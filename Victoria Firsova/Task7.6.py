"""Task 7.6. Create console program for proving Goldbach's conjecture.
Program accepts number for input and print result.
For pressing 'q' program succesfully close. Use function from Task 5.5 for validating input,
 handle all exceptions and print user friendly output."""
from argparse import ArgumentParser
import sys


def parser_arguments():
    """Getting values from the command line"""

    parser = ArgumentParser(usage='number [-h] [q]', description='program for proving Goldbach\'s conjecture')
    parser.add_argument('number', nargs='?', help='Input a number that is even and > 4')
    parser.add_argument('--q', action="store_true",default = False, help='program exit')

    args = parser.parse_args()
    result = vars(args)
    return result

def validation_input(num):
    result = None
    try :
        num = int(num)
        if num % 2 == 0 and num > 4:
            result = "Number is even. It's ok"
        else :
            raise Exception('Number is not even')

    except ValueError :
        print("It's not an int")
        sys.exit()
    except Exception:
        print('Number is not even')
        sys.exit()

    return result

def proving_conjecture(num, lst):

    for i in lst[::-1]:
        a = num - i
        if a in lst:
            print(f'{i}+{a}={num}. Goldbach\'s conjecture is prooved')
            break


def prime_number(num):
    n = num
    lst = [2]
    for i in range(3, n + 1, 2) :
        if (i > 10) and (i % 10 == 5) :
            continue
        for j in lst :
            if j * j - 1 > i :
                lst.append(i)
                break
            if (i % j == 0) :
                break
        else :
            lst.append(i)
    return lst


if __name__ == '__main__':
    result = parser_arguments()
    if result['q']:
        exit()
    num = result['number']
    validation_input(num)
    num = int(result['number'])
    lst = prime_number(num)
    proving_conjecture(num, lst)
