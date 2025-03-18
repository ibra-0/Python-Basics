import math

# 1. Конвертация градусов в радианы
def degrees_to_radians(degrees):
    return round(degrees * (math.pi / 180), 6)

print("Output radian:", degrees_to_radians(15))

# 2. Площадь трапеции
def trapezoid_area(height, base1, base2):
    return 0.5 * (base1 + base2) * height

print("Expected Output:", trapezoid_area(5, 5, 6))

# 3. Площадь правильного многоугольника
def regular_polygon_area(sides, length):
    return round((sides * (length ** 2)) / (4 * math.tan(math.pi / sides)), 2)

print("The area of the polygon is:", regular_polygon_area(4, 25))

# 4. Площадь параллелограмма
def parallelogram_area(base, height):
    return base * height

print("Expected Output:", parallelogram_area(5, 6))
