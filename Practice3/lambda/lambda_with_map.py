# lambda_with_map.py

numbers = [1, 2, 3, 4]

# Квадраты чисел
squares = list(map(lambda x: x ** 2, numbers))
print(squares)

# Умножение на 10
times_ten = list(map(lambda x: x * 10, numbers))
print(times_ten)