# Day10 Project
# Student Management System V2

students = []

def add_student():

    try:
        name = input("Enter Student Name: ")
        marks = int(input("Enter Marks: "))
        student = {
            "name": name,
            "marks": marks
        }
        students.append(student)
        print("Student added successfully!")
    except ValueError:
        print("Marks must be a number.")

def view_students():
    if len(students) == 0:
        print("No Student records found.")
        return
    print("\n---STUDENT LIST---")
    for i, student in enumerate(students, start=1):
        print("\nStudent", i)
        print("Name :", student["name"])
        print("Marks :", student["marks"])

def save_students():
    file = open("students.txt", "w")

    for student in students:
        file.write(
            student["name"] + "," +
            str(student["marks"]) + "\n"
        )
    file.close()
    print("Data Saved Successfully!")

while True:
    print("\n===STUDENT MANAGEMENT SYSTEM===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Save Students")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        save_students()
    elif choice == "4":
        print("Program Closed.")
        break
    else:
        print("Invalid Choice")
