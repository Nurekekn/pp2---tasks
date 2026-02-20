
# 1️⃣ Простое переопределение
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

d = Dog()
d.speak()

print("-----")

# 2️⃣ Переопределение с super()
class Bird:
    def fly(self):
        print("Bird flies")

class Eagle(Bird):
    def fly(self):
        super().fly()
        print("Eagle flies high")

e = Eagle()
e.fly()

print("-----")

# 3️⃣ Полная замена логики
class Shape:
    def area(self):
        print("Unknown area")

class Square(Shape):
    def area(self):
        print("Area of square calculated")

sq = Square()
sq.area()

print("-----")

# 4️⃣ Разное поведение у разных потомков
class Employee:
    def work(self):
        print("Employee works")

class Developer(Employee):
    def work(self):
        print("Developer writes code")

class Designer(Employee):
    def work(self):
        print("Designer creates UI")

dev = Developer()
des = Designer()
dev.work()
des.work()