import os
import shutil
import string
from functools import reduce
import time
import math

def list_items(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return directories, files

def check_access(path):
    return {
        "exists": os.path.exists(path),
        "readable": os.access(path, os.R_OK),
        "writable": os.access(path, os.W_OK),
        "executable": os.access(path, os.X_OK)
    }

def path_info(path):
    if os.path.exists(path):
        return os.path.dirname(path), os.path.basename(path)
    return None

def count_lines(filename):
    with open(filename, 'r') as file:
        return sum(1 for _ in file)

def write_list_to_file(filename, lst):
    with open(filename, 'w') as file:
        file.writelines(f"{item}\n" for item in lst)

def generate_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as file:
            file.write(f"This is {letter}.txt\n")

def copy_file(src, dest):
    shutil.copy(src, dest)

def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        return f"File {path} deleted successfully."
    return "File does not exist or cannot be deleted."

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