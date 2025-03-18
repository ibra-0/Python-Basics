'''def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial_iterative(5)) '''

'''class Car:
     def __init__(self, brand, model):
        self.brand = brand
        self.model = model

     def start(self):
        print("Car is starting...")

class ElectricCar(Car):  
    def start(self):
        print("Electric Car is starting silently...")
car1 = Car("BMW", "M5")
car1.start()  

ev1 = ElectricCar("Porsche", "Taycan")
ev1.start()    '''

"""def even_numbers():
    num = 0
    while True:
        yield num
        num += 2  

gen = even_numbers()  
print(next(gen))
print(next(gen))
print(next(gen))"""

"""from datetime import datetime, timedelta


def add_five_days():
    return datetime.today() + timedelta(days=5)  
print(add_five_days().date())  """

import re

text = "Аня, Аля, Ася, ФТРб, оутЭэ."

pattern = r"\bА\wя\b"  

matches = re.findall(pattern, text)

print(matches) 
