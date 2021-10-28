"""Task 7.4. Implement decorator for suppressing exceptions.
If exception not occur write log to console."""
import logging


def suppressing_exceptions(func):
    def wrapped(*args):
        try:
            logging.basicConfig(level=logging.INFO)
            result = func(*args)
            logging.info("Wrapping the func and write a result to variable 'result'")
            return result
        except BaseException:
            print('Exception occurred')

    return wrapped


@suppressing_exceptions
def division(a=int):
    a = a + 3
    if type(a) is str:
        raise BaseException
    return a

print(division('a'))
