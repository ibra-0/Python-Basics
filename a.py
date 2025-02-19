'''def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial_iterative(5)) '''

class Car:
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
ev1.start()    