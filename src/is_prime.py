from math import sqrt
import sys


def check(n):
    """Check if a number is prime, return True if it is False otherwise.

    Args:
    n -- the number to check for primeness
    """
    if n == 1:
        return True
    elif (n % 2 == 0) and (n != 2):
        return False
    else:
        for x in range(3, (int(sqrt(n)) + 1)):
            if n % x == 0:
                return False
        return True


def build_matrix(indices):
    return False


def print_matrix(size):
    """Print a multiplication table with Prime numbers as the Row and Column Indeces.  The matrix
    will be populated with the Products of the Prime numbers.

    Args:
    size  -- the amount of prime numbers to find, starting with 1
    """
    indices = []
    for i in range(sys.maxsize):
        if check(i):
            indices.append(i)
        if len(indices) == 10:
            break

    print(indices)


if __name__=='__main__':
    print_matrix(10)
