
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
#chek
# 1 класс
class Dog:
    def _init_(self, name):
        self.name = name

    def bark(self):
        print(self.name, "says Woof!")


# 2 класс
class Cat:
    def _init_(self, name):
        self.name = name

    def meow(self):
        print(self.name, "says Meow!")


# 3 класс
class Car:
    def _init_(self, brand):
        self.brand = brand

    def drive(self):
        print(self.brand, "is driving.")


# 4 класс
class Student:
    def _init_(self, name):
        self.name = name

    def study(self):
        print(self.name, "is studying.")


# 🔹 Использование классов

dog1 = Dog("Buddy")
cat1 = Cat("Milo")
car1 = Car("BMW")
student1 = Student("Anna")

dog1.bark()
cat1.meow()
car1.drive()
student1.study()
#4e5
# 1) Базовый класс
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"Person: {self.name}, age {self.age}"


# 2) Наследник №1
class Student(Person):
    def _init_(self, name, age, university):
        super()._init(name, age)          # <-- super() вызывает Person.init_
        self.university = university

    def info(self):
        base = super().info()                 # <-- super() вызывает Person.info
        return f"{base}, university {self.university}"


# 3) Наследник №2
class Staff(Person):
    def _init_(self, name, age, position):
        super()._init_(name, age)
        self.position = position

    def info(self):
        base = super().info()
        return f"{base}, position {self.position}"


# 4) Наследник от наследника (4-й класс)
class TeachingAssistant(Student):
    def _init_(self, name, age, university, course):
        super()._init(name, age, university)  # <-- super() вызывает Student.init_
        self.course = course

    def info(self):
        base = super().info()                    # <-- super() вызывает Student.info
        return f"{base}, assists course {self.course}"


# --- Использование классов (создание объектов) ---
p = Person("Aida", 20)
s = Student("Nurdana", 19, "KBTU")
st = Staff("Timur", 28, "Administrator")
ta = TeachingAssistant("Dana", 20, "KBTU", "OOP")

print(p.info())
print(s.info())
print(st.info())
print(ta.info())