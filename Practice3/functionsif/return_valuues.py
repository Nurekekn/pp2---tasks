
# 1. Возврат суммы
def add(a, b):
    return a + b

result = add(10, 5)
print(result)

# 2. Возврат строки
def full_name(first, last):
    return first + " " + last

print(full_name("John", "Doe"))

# 3. Возврат списка
def create_list():
    return [1, 2, 3]

print(create_list())

# 4. Возврат True/False
def is_even(num):
    return num % 2 == 0

print(is_even(4))