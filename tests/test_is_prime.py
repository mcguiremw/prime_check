import pytest

from src.is_prime import check


def test_int_one():
    assert check(1) is True

def test_int_two():
    assert check(2) is True

def test_int_three():
    assert check(3) is False
