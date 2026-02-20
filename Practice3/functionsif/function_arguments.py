

# 1. Позиционные аргументы
def multiply(a, b):
    print(a * b)

multiply(4, 5)

# 2. Именованные аргументы
multiply(b=3, a=6)

# 3. Значение по умолчанию
def greet(name="Guest"):
    print("Hello,", name)

greet()
greet("Maria")

# 4. Необязательный аргумент
def power(base, exponent=2):
    print(base ** exponent)

power(3)
power(3, 3)