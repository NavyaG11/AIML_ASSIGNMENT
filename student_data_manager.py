students = {
    "Rahul": 85,
    "Anita": 92,
    "Kiran": 78,
    "Sneha": 88,
    "Arjun": 95
}

total = 0
topper = ""
highest = 0

for name, marks in students.items():
    total += marks
    if marks > highest:
        highest = marks
        topper = name

average = total / len(students)

print("Topper:", topper, "-", highest)
print("Class Average:", average)

print("\nGrades:")
for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    else:
        grade = "C"

    print(name, ":", grade)