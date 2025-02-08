'''class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)'''


#Python Classes
'''class StringProcessor:
    def __init__(self):
        self.text = ""


    def getstring(self):
        self.text = input("Введите строку: ")


    def printString(self):
        print(self.text.upper())
'''

class Shape:
    def __init__(self):
        self.area = 0


    def printArea(self):
        print(f"Площадь: {self.area}")   

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
        self.area = length * length

sq = Square(4)
sq.printArea()

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        self.area = length * width  

rect = Rectangle(4, 5)
rect.printArea() 




            

        