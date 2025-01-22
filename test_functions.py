import pytest
from functions import add, subtract, divide


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(-1, -1) == 0
    assert subtract(0, 5) == -5

def test_division():
    assert divide(6, 2) == 3

def test_division_error():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

"""
To run the tests, execute the following command in the terminal:
pytest test_functions.py
or just: pytest
"""
