### 1.3 Email verification
# A collegue of yours has managed to produce this function for checking if an input is a valid email address.

import re
#RegEx Module: because using r in the email_pattern string.
# In Python, the r before a string indicates that the string is a raw string literal.
# This means that backslashes (\) in the string are treated literally and do not escape characters as they normally would in a regular string.


def is_email(address):
    # Check if the input string is a valid email address.
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, address))


#^[^@]+ : Ensures at least one character before the @ symbol.
# @[a-zA-Z0-9.-]+ : Matches the domain part with valid characters.
# \.[a-zA-Z]{2,}$ : Ensures at least one . followed by two or more alphabetic characters for the domain suffix.


# You feel (rightly so) that the function is hard to read, but you have more pressing matters and this function will soon be a part of the main code base.
# However, since you have a hard time intuitively understanding the function, it is very important that you write some tests for it.
# Write some tests for is_email() with both valid and invalid email-addresses as inputs.

# A valid address is defined as:
# - The email has one @ symbol.
# - At least one character before @, and at least one dot (.) after @.
# - The domain part (after @) has at least two characters.

import pytest

def test_valid_email_simple():
    assert is_email("user@example.com") == True  # Valid

def test_valid_email_with_subdomain():
    assert is_email("user@sub.example.com") == True  # Valid

def test_missing_at_symbol():
    assert is_email("userexample.com") == False  # InValid - Missing '@'

def test_missing_character_before_at():
    assert is_email("@example.com") == False  # InValid - No character before '@'

def test_missing_dot_after_at():
    assert is_email("user@examplecom") == False  # InValid - No '.' after '@'

def test_domain_too_short():
    assert is_email("user@e.co") == True       # Valid - Single character after `@`
    assert is_email("user@e.c") == False       # InValid - Less than two characters in domain

def test_extra_at_symbols():
    assert is_email("user@domain@domain@domain.com") == False  # InValid

def test_empty_string():
    assert is_email("") == False  # InValid - Empty string

def test_valid_email_with_special_characters():
    assert is_email("user.name+alias@domain.com") == True  # Valid email with special characters

def test_single_character_domain():
    assert is_email("user@e.com") == True  # Valid

def test_valid_email_with_special_characters():
    assert is_email("user.name+alias@domain.com") == True  # Valid email with special characters

def test_single_character_user():
    assert is_email("a@domain.com") == True   # Valid

def test_dot_user():
    assert is_email(".@domain.com") == True # InValid

def test_only_special_character_user():
    assert is_email("._%@domain.com") == True # InValid

def test_leading_dot_user():
    assert is_email("...user@domain.com") == True #InValid

def test_invalid_character_in_domain():
    assert is_email("user@---.com") == True # InValid



# def is_email(address):
    # Improved regex pattern for validating an email address
#    email_pattern = r'^(?!.*\.\.)(?!.*\.$)(?!.*\.$)(?!.*@.*@)[^@]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#    return bool(re.match(email_pattern, address))

# (?!.*@.*@): Prevents multiple @ symbols.
# (?!.*\.\.): Disallows consecutive dots in the local part.
# (?!.*\.$): Disallows trailing dots in the local part.
# [^@]+: Ensures at least one character before the @.

# pytest -v MeMailVerificationSolution.py