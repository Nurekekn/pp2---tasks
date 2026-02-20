temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")
#2
username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")
#3
a = 5
b = 2
if a > b: print("a is greater than b")
#4
a = 2
b = 330
print("A") if a > b else print("B")
#4
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)
#5
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

