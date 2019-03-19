import pytest

from src.is_prime import check


def test_first_ten_primes():
    first_ten = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
    assert len(first_ten) == 10

    for n in first_ten:
        assert check(n) is True
