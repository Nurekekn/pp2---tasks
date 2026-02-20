
# 1️⃣ Простое наследование
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass

d = Dog()
d.speak()

print("-----")

# 2️⃣ Наследование с добавлением метода
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

c = Car()
c.start()
c.drive()

print("-----")

# 3️⃣ Проверка типа
class Person:
    pass

class Student(Person):
    pass

s = Student()
print(isinstance(s, Student))
print(isinstance(s, Person))

print("-----")

# 4️⃣ Доступ к атрибуту родителя
class Parent:
    message = "Hello from Parent"

class Child(Parent):
    pass

child = Child()
print(child.message)