# 1.2 Blast to the past!
# Visit a function that you have written previously in the course, your choice.
# Write some tests for this function with different inputs.

import pytest

# Pytesting for this function will ALWAYS return PASSED !!!
# Since the function only creats a dictionary and takes no argument in.
# This function is not a good one to learn about Pytest

#def CreateSquare_dict_function():
#    square_dict = {i: i ** 2 for i in range(1, 11)}
#    return square_dict
#def test_CreateSquareDic():
#    assert CreateSquare_dict_function()

# We are giong to Pytest a function which takes an argument in and returns a value:
def fibonacci(n):
    f0 = 0
    f1 = 1
    
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return f0
    elif n == 1:
        return f1
    else:
        for i in range(1, n):
            fn = f0 + f1
            f0 = f1
            f1 = fn
        return f1


def test_fibonacci_zero():
    assert fibonacci(0) == 0  # Fibonacci of 0 is 0

def test_fibonacci_one():
    assert fibonacci(1) == 1  # Fibonacci of 1 is 1

def test_fibonacci_small_number():
    assert fibonacci(5) == 5  # Fibonacci of 5 is 5

def test_fibonacci_larger_number():
    assert fibonacci(10) == 55  # Fibonacci of 10 is 55

def test_fibonacci_negative():
    assert fibonacci(-5) == None  # Negative input should return None

def test_fibonacci_large():
    assert fibonacci(20) == 6765  # Fibonacci of 20 is 6765

# Spoiler alert: this one should fail
def test_fibonacci_failing_test():
    assert fibonacci(10) == 100  # Fibonacci of 10 is 55

# pytest -v MPastSolution.py