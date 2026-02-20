
# 1️⃣ super() в __init__
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Anna", "A")
print(s.name, s.grade)

print("-----")

# 2️⃣ super() в обычном методе
class Animal:
    def speak(self):
        print("Animal sound")

class Cat(Animal):
    def speak(self):
        super().speak()
        print("Meow")

c = Cat()
c.speak()

print("-----")

# 3️⃣ Добавление логики после super()
class Vehicle:
    def start(self):
        print("Engine started")

class ElectricCar(Vehicle):
    def start(self):
        super().start()
        print("Battery activated")

ec = ElectricCar()
ec.start()

print("-----")

# 4️⃣ super() с несколькими параметрами
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

m = Manager("Tom", 5000, "IT")
print(m.name, m.salary, m.department)