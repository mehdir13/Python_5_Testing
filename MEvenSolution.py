### 1.1 isEven(n)
# Write a function isEven(n) that takes in a number and determines if it is even.
# Then, write some appropiate tests for it.

import pytest

# SCENARIO 1:
# We write the function, and then try to call it by assigning user input as function's parameter:

# def is_even(number):
#       return number %2 == 0
# num = int(input("PLEASE Enter a number: "))
# if is_even(num):
#       print(f"{num} is even")
# else:
#       print(f"{num} is odd")
#AND NOW RUN PYTEST:
# def test_isEven():
#    assert is_even(0) == True
#    assert is_even(1) == False
#    assert is_even(2) == True
#    assert is_even(3) == True
#    assert is_even(4) == False
#    assert is_even(5) == True

# The result will be error in Pytest: 
# ERROR collecting MEvenSolution.py ________________________________________________________________
# MEvenSolution.py:8: in <module>
#    num = int(input("PLEASE Enter a number: "))
#..\..\..\AppData\Local\Programs\Python\Python313\Lib\site-packages\_pytest\capture.py:209: in read
#    raise OSError(
#E   OSError: pytest: reading from stdin while output is captured!  Consider using -s.

# The reason is that: 
# The error you're seeing occurs because pytest is trying to capture output, but input() is blocking it.
# To make your tests work, we should avoid using input() directly in the code we want to test.
# Solution:
# To make pytest work seamlessly, let’s separate the interactive part of the program from the function and modify the test to focus solely on is_odd.
# Updated Code Structure:
# 1. Refactor is_odd() function:
# Make sure is_odd() does not rely on input() directly but instead accepts arguments.
# 2. Write tests for the is_odd() function independently of the input() call.

#LESSON LEARNED: when Pytestin a function, we need only and only the function itself, not the calling and parameter assignment.

# SCENARIO 2:
# We rewrite the code but this time we write only the function and Pytest the dunction.

def is_even(number):
    return number %2 == 0


def test_even_number():
    assert is_even(4) == True  # 4 is even

def test_odd_number():
    assert is_even(5) == False  # 5 is odd

def test_zero():
    assert is_even(0) == True  # 0 is even

def test_negative_even_number():
    assert is_even(-2) == True  # -2 is even

def test_negative_odd_number():
    assert is_even(-3) == False  # -3 is odd
 
# Spoiler alert: this one should fail.
def test_failing_number():
    assert is_even(5) == True  # -3 is odd

# write in command line: pytest -v MEvenSolution.py