
# 1️⃣ 
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

print("-----")

# 2️⃣ 
num = 0
while num <= 10:
    num += 1
    if num % 2 != 0:
        continue
    print("Even:", num)

print("-----")

# 3️⃣ 
numbers = [3, -1, 5, -7, 9]
i = 0
while i < len(numbers):
    if numbers[i] < 0:
        i += 1
        continue
    print(numbers[i])
    i += 1

print("-----")

# 4️⃣
divisors = [5, 0, 2]
i = 0
while i < len(divisors):
    if divisors[i] == 0:
        i += 1
        continue
    print(10 / divisors[i])
    i += 1

print("-----")

# 5️⃣ 
words = ["hello", "skip", "world"]
i = 0
while i < len(words):
    if words[i] == "skip":
        i += 1
        continue
    print(words[i])
    i += 1