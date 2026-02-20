
# 1️⃣ Базовый конструктор
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Alex")
print(p1.name)

print("-----")

# 2️⃣ Несколько параметров
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s1 = Student("Anna", "A")
print(s1.name, s1.grade)

print("-----")

# 3️⃣ Значение по умолчанию
class Car:
    def __init__(self, brand="BMW"):
        self.brand = brand

c1 = Car()
c2 = Car("Audi")
print(c1.brand)
print(c2.brand)

print("-----")

# 4️⃣ Вычисление внутри конструктора
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height

r1 = Rectangle(5, 3)
print("Area:", r1.area)