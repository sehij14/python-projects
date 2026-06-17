import json

students = [
    {
        "name": "Rahul",
        "age": 18,
        "marks": 90,
        "grade": "B"
    },
    {
        "name": "Aman",
        "age": 19,
        "marks": 85,
        "grade": "B"
    },
    {
        "name": "Priya",
        "age": 18,
        "marks": 95,
        "grade": "A"
    }
]

# Save Data

file = open("students.json", "w")

json.dump(students, file, indent=4)

file.close()

print("Student data saved successfully!")

# Read Data

file = open("students.json", "r")

data = json.load(file)

file.close()

print("\n----- STUDENT DATABASE -----")

for student in data:

    print("\nName:", student["name"])

    print("Age:", student["age"])

    print("Marks:", student["marks"])

    print("Grade:", student["grade"])