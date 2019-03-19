from src.is_prime import build_matrix, check


def test_check_zero():
    assert check(0) == False


def test_first_ten_primes():
    first_ten = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
    assert len(first_ten) == 10

    for n in first_ten:
        assert check(n) is True


def test_non_prime_from_first_ten():
    non_prime = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22]
    assert len(non_prime) == 13

    for n in non_prime:
        assert check(n) == False


def test_large_int_not_prime():
    dev_sys_maxint = 9223372036854775807
    assert check(dev_sys_maxint) == False


def test_large_int_prime():
    openssl_gen_prime = 896566843
    assert check(openssl_gen_prime) == True

def test_build_matrix():
    expected_matrix = [[1, 2, 3, 5], [2, 4, 6, 10], [3, 6, 9, 15], [5, 10, 15, 25]]
    assert build_matrix(4) == expected_matrix
