"""Task 7.2. Implement context manager for opening and working with file,
including handling exceptions with @contextmanager decorator."""

from contextlib import contextmanager


@contextmanager
def file_open(path):
    try:
        file = open(path, 'w')
        yield file
    except FileExistsError:
        print('Wrong path')  
    except OSError:
        print("We had an error!")
    finally:
        f_obj.close()
