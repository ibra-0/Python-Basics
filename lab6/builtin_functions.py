from functools import reduce
import time
import math

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

def count_case(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    return upper, lower

def is_palindrome(s):
    return s == s[::-1]

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)  # Convert milliseconds to seconds
    return math.sqrt(number)

def all_true(t):
    return all(t)

# Sample usage
print(multiply_list([1, 2, 3, 4]))  # Output: 24

upper, lower = count_case("Hello World")
print(f"Uppercase: {upper}, Lowercase: {lower}")

print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False

number = 25100
delay = 2123
print(f"Square root of {number} after {delay} milliseconds is {delayed_sqrt(number, delay)}")

print(all_true((True, True, False)))  # Output: False
print(all_true((True, True, True)))   # Output: True
