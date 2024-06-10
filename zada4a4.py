data = [
    "Peter:23:I-ви курс"
    "Ivan:10:II-ти курс"
    "Maya:24:II-ти курс"
    "Lily:13:II-ти курс"
]
target_class = input()
students = {}
for i in data:
    name, number, classes = i.split(':')
    if classes not in students:
        students[classes] = {}
    students[classes][name] = int(number)
if target_class in students:
    for name, number in students[target_class].items():
        print(f"{name}: {number}")
else:
    print(f"Няма ученици в клас {target_class}")
