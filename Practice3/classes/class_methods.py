
# 1️⃣ Instance method
class Person:
    def greet(self):
        print("Hello!")

p1 = Person()
p1.greet()

print("-----")

# 2️⃣ Class method
class Employee:
    company = "Google"

    @classmethod
    def show_company(cls):
        print("Company:", cls.company)

Employee.show_company()

print("-----")

# 3️⃣ Static method
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(4, 6))

print("-----")

# 4️⃣ Изменение class variable через class method
class School:
    name = "Old School"

    @classmethod
    def change_name(cls, new_name):
        cls.name = new_name

School.change_name("New School")
print(School.name)