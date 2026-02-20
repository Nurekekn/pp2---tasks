
#  
num = 1
while num <= 10:
    if num == 5:
        break
    print(num)
    num += 1

print("-----")

# 2️⃣ 
numbers = [3, 7, 2, 9, 5]
i = 0
while i < len(numbers):
    if numbers[i] == 9:
        print("Found 9!")
        break
    i += 1

print("-----")

# 3️⃣ 
while True:
    text = input("Type 'exit' to stop: ")
    if text == "exit":
        break

print("Stopped")

print("-----")

# 4️⃣ 
n = 5
while n > -5:
    if n < 0:
        break
    print(n)
    n -= 1

print("-----")

# 5️⃣ 
nums = [1, 3, 5, 8, 9]
i = 0
while i < len(nums):
    if nums[i] % 2 == 0:
        print("First even:", nums[i])
        break
    i += 1