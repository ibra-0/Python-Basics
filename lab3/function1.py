import random
import itertools

# 1
def grams_to_ounces(grams):
    return 28.3495231 * grams

# 2
def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

# 3
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None

# 4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

# 5
def string_permutations(s):
    return [''.join(p) for p in itertools.permutations(s)]

# 6
def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

# 7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1] == 3:
            return True
    return False

# 8
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

# 9
def sphere_volume(radius):
    return (4 / 3) * 3.141592653589793 * radius ** 3

# 10
def unique_elements(lst):
    unique_list = []
    for elem in lst:
        if elem not in unique_list:
            unique_list.append(elem)
    return unique_list

# 11.
def is_palindrome(word):
    return word == word[::-1]

# 12.
def histogram(lst):
    for num in lst:
        print('*' * num)

# 13
def guess_number():
    name = input("Hello! What is your name?\n")
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

    number = random.randint(1, 20)
    attempts = 0

    while True:
        guess = int(input("\nTake a guess.\n"))
        attempts += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break

# 14. 
if __name__ == "__main__":
    print(grams_to_ounces(10))  
    print(fahrenheit_to_celsius(100))
    print(solve(35, 94))
    print(filter_prime([1, 2, 3, 4, 5, 11, 13, 17]))
    print(string_permutations("abc"))
    print(reverse_sentence("We are ready"))
    print(has_33([1, 3, 3]))
    print(spy_game([1, 2, 4, 0, 0, 7, 5]))
    print(sphere_volume(3))
    print(unique_elements([1, 2, 2, 3, 4, 4, 5]))
    print(is_palindrome("madam"))
    histogram([4, 9, 7])
   
    
