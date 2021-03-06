import argparse
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


def build_matrix(size):
    """Given the amount of prime numbers to find, build a two dimensional array with the prime
    numbers as the indices for the rows and columns.  Each cell will be the product of their
    respective row and column indices, return the resulting matrix.

    Args:
    size -- the amount of prime numbers to find, starting with 1
    """
    indices = []
    for i in range(sys.maxsize):
        if check(i):
            indices.append(i)
        if len(indices) == size:
           break

    return [[x*y for x in indices] for y in indices]


def print_matrix(size):
    """Print a multiplication table with prime numbers as the Row and Column Indeces.

    Args:
    size  -- the amount of prime numbers to find, starting with 1
    """
    matrix = build_matrix(size)
    for x in matrix:
        print(*x, sep="\t")


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Print a Multiplication Table of Primary Numbers')
    parser.add_argument(
        '--primes', nargs='?', const=1, default=10, type=int,
        help='How many primes would you like to build the multiplication table with?')
    print_matrix(parser.parse_args().primes)
