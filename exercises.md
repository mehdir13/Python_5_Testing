### 1.1 isEven(n)

Write a function isEven(n) that takes in a number and determines if it is even. Then, write some appropiate tests for it.

### 1.2 Blast to the past!

Visit a function that you have written previously in the course, your choice. Write some tests for this function with different inputs.

## Harder exercises

### 1.3 Email verification

A collegue of yours has managed to produce this function for checking if an input is a valid email address.

```
import re

def is_email(address):
    """Check if the input string is a valid email address."""
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, address))

```

You feel (rightly so) that the function is hard to read, but you have more pressing matters and this function will soon be a part of the main code base. However, since you have a hard time intuitively understanding the function, it is very important that you write some tests for it. Write some tests for is_email() with both valid and invalid email-addresses as inputs.

A valid address is defined as:

- The email has one @ symbol.
- At least one character before @, and at least one dot (.) after @.
- The domain part (after @) has at least two characters.

### 1.4 isPrime(n)

Read up on what a prime number is, either through ChatGPT or articles online. For example, 11 is a prime number because there is not integer except one or 11 which can divide it. 9 on the other hand is not a prime number because 3 can divide it. 9 / 3 = 3.

Now consider the function:

```
def is_prime(n):
    """Check if a number is prime."""
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

```

I have written this function to check if a number is prime or not. Your task is to implement a few tests for this function. Test a few different numbers and see if you get the expected result.
