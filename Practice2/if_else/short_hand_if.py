x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)
#2
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)
#3
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
#4
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
#5
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")