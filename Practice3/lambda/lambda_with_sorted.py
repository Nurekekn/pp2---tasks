# lambda_with_sorted.py

students = [
    {"name": "Anna", "grade": 85},
    {"name": "Tom", "grade": 92},
    {"name": "John", "grade": 78}
]

# Сортировка по оценке
sorted_students = sorted(students, key=lambda x: x["grade"])
print(sorted_students)