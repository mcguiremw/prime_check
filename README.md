## Requirements
- Run from the command line
    - Default:
        - No user input
        - Calculate first 10 prime numbers
    - Optional:
        - Pass in single integer, calculate all primes up to that int
- Print Matrix of Prime Numbers and their product
    - Index Row x Col are the Prime numbers
    - Products of `r*c` populate matrix
- Able to test single int with time complexity of `O(log(n))`

## Running the Code
- This project was developed using Python 3.7.1 but any version of Python3 _should_ work
- Install required packages
    - `pip install -r requirements.txt`

## Running the Tests
- From the root directory of the project run the tests using *Pytest*
    - `pytest -v`
- Pytest would have been installed from the _requirements.txt_ file see [Running the
  Code](#running-the-code)

## Performance Considerations
### Finding a large non prime number is fairly easy
```
from src.is_prime import check

timeit(check(sys.maxsize))
1.32 µs ± 11.2 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
```

### Verifying a large Prime number is much more computationally expensive
Using the OpenSSL Command Line Tool we are able to generate prime numbers to work with
- `openssl prime -generate -bits 50`
```
timeit(check(987608350166551))
3.13 s ± 43.6 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

- `openssl prime -generate -bits 60`
```
timeit(check(964323014774268299))
1min 42s ± 1.3 s per loop (mean ± std. dev. of 7 runs, 1 loop each)
```
