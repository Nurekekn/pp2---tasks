
numbers = [1, 2, 3, 4, 5, 6]

# Только четные
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# Больше 3
greater = list(filter(lambda x: x > 3, numbers))
print(greater)