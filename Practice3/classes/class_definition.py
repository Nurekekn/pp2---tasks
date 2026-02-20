
# 1️⃣ Простой класс
class Person:
    def greet(self):
        print("Hello!")

p1 = Person()
p1.greet()

print("-----")

# 2️⃣ Класс с атрибутом класса
class Car:
    brand = "Toyota"

car1 = Car()
print(car1.brand)

print("-----")

# 3️⃣ Класс с методом
class Animal:
    def speak(self):
        print("Animal makes a sound")

a1 = Animal()
a1.speak()

print("-----")

# 4️⃣ Класс с несколькими методами
class Calculator:
    def add(self, a, b):
        print(a + b)

    def subtract(self, a, b):
        print(a - b)

calc = Calculator()
calc.add(10, 5)
calc.subtract(10, 5)