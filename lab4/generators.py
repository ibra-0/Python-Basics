# 1. Генератор квадратов чисел до N

def square_generator(N):
    for i in range(N + 1):
        yield i ** 2

# 2. Генератор четных чисел до n

def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter a number: "))
print(", ".join(map(str, even_numbers(n))))

# 3. Генератор чисел, делящихся на 3 и 4, до n

def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# 4. Генератор квадратов чисел от a до b

def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

for sq in squares(3, 8):
    print(sq)

# 5. Генератор чисел от n до 0

def countdown(n):
    for i in range(n, -1, -1):
        yield i

for num in countdown(5):
    print(num)