adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#2
for x in [0, 1, 2]:
  pass
#3
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

print("-----")
#4
num = 2
while num <= 10:
    print("Even:", num)
    num += 2
#5
password = ""
while password != "admin":
    password = input("Enter password: ")
print("Access granted!")

print("-----")