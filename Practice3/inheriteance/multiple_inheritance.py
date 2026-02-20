
# 1️⃣ Базовый пример
class Father:
    def skills(self):
        print("Programming")

class Mother:
    def design(self):
        print("Design")

class Child(Father, Mother):
    pass

c = Child()
c.skills()
c.design()

print("-----")

# 2️⃣ Порядок наследования (MRO)
class A:
    def show(self):
        print("Class A")

class B:
    def show(self):
        print("Class B")

class C(A, B):
    pass

obj = C()
obj.show()  # Берется метод из A

print("-----")

# 3️⃣ super() при multiple inheritance
class Base:
    def greet(self):
        print("Hello from Base")

class Parent1(Base):
    pass

class Parent2(Base):
    pass

class Child(Parent1, Parent2):
    pass

child = Child()
child.greet()

print("-----")

# 4️⃣ Комбинирование функциональности
class Engine:
    def start_engine(self):
        print("Engine started")

class GPS:
    def navigate(self):
        print("Navigation started")

class SmartCar(Engine, GPS):
    pass

sc = SmartCar()
sc.start_engine()
sc.navigate()