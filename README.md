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
- Able to test single int with time complexity of O(1)

## Running the Code
- This project was developed using Python 3.7.1 but any version of Python3 _should_ work
- Install required packages
    - `pip install -r requirements.txt`

## Running the Tests
- From the root directory of the project run the tests using *Pytest*
- Pytest would have been installed from the _requirements.txt_ file see [Running the
  Code](#running-the-code)


## Consider
- Profile with Snakeviz for submission
- Seperate function for printing, allows for testing without dumping to STDOUT
