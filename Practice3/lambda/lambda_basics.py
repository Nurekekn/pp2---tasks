
# 1. Простая lambda
add = lambda a, b: a + b
print(add(5, 3))

# 2. Квадрат числа
square = lambda x: x ** 2
print(square(4))

# 3. Проверка четности
is_even = lambda x: x % 2 == 0
print(is_even(10))

# 4. Конкатенация строк
full_name = lambda f, l: f + " " + l
print(full_name("John", "Smith"))