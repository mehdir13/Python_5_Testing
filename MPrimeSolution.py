### 1.4 isPrime(n)
# Read up on what a prime number is, either through ChatGPT or articles online. For example, 11 is a prime number because there is not integer except one or 11 which can divide it. 9 on the other hand is not a prime number because 3 can divide it. 9 / 3 = 3.
# Now consider the function:

def is_prime(n):
    # Check if a number is prime.
    if n <= 1:
        return False  # 0, 1, and negative numbers are not prime
    if n <= 3:
        return True   # 2 and 3 are prime numbers
    if n % 2 == 0 or n % 3 == 0:
        return False  # Multiple of 2 or 3 are not prime

    # Check for factors from 5 to the square root of n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True



# I have written this function to check if a number is prime or not.
# Your task is to implement a few tests for this function.
# Test a few different numbers and see if you get the expected result.

def test_is_prime():
    assert is_prime(0) == False  # 0 is not prime
    assert is_prime(1) == False  # 1 is not prime
    assert is_prime(2) == True   # 2 is prime
    assert is_prime(3) == True   # 3 is prime
    assert is_prime(4) == False  # 4 is not prime
    assert is_prime(5) == True   # 5 is prime
    assert is_prime(9) == False  # 9 is not prime (3*3)
    assert is_prime(11) == True   # 11 is prime
    assert is_prime(25) == False  # 25 is not prime (5*5)
    assert is_prime(29) == True   # 29 is prime
    assert is_prime(97) == True   # 97 is prime
    assert is_prime(100) == False  # 100 is not prime
    assert is_prime(101) == True   # 101 is prime
    assert is_prime(121) == False  # 121 is not prime (11*11)

def test_extra_large_non_prime():
    assert is_prime(10**6) == False  # 1,000,000
    assert is_prime(10**6 + 1) == False  # 1,000,001
    assert is_prime(10**6 + 9) == False  # 1,000,009
    assert is_prime(10**6 + 25) == False  # 1,000,025
    assert is_prime(10**7) == False  # 10,000,000
    assert is_prime(10**7 + 1) == False  # 10,000,001
    assert is_prime(10**7 + 5) == False  # 10,000,005





import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the starting time of the original function
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record the ending time of the original function
        execution_time = end_time - start_time
        print(f"Execution time is: {execution_time:.4f} seconds")
        return result  # Return the original function's result
    return wrapper

# a slow function
@timer
def test_extra_large_prime_in_Fibonacci():
 assert is_prime(2971215073) == True                       # .0026 seconds
 assert is_prime(99194853094755497) == True                # 13.59 seconds
 #assert is_prime(1066340417491710595814572169) == True    # TOO BIG FOR MY LAPTOP over 2 minutes and I stopped the program
 #assert is_prime(19134702400093278081449423917) == True   # TOO BIG FOR MY LAPTOP
 

# pytest -v MPrimeSolution.py