
# 1️⃣ Простой пример
class Dog:
    species = "Canine"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.species)
print(dog2.species)

print("-----")

# 2️⃣ Изменение class variable
Dog.species = "Wolf"
print(dog1.species)
print(dog2.species)

print("-----")

# 3️⃣ Переопределение instance variable
dog1.species = "Fox"
print(dog1.species)  # instance override
print(dog2.species)  # still class value

print("-----")

# 4️⃣ Подсчет созданных объектов
class Counter:
    count = 0  # class variable

    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
c3 = Counter()

print("Objects created:", Counter.count)