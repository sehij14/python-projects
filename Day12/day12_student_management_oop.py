# Day 12 Project
# Student Management System Using OOP

class Student:

    def __init__(self, name, age, marks):

        self.name = name
        self.age = age
        self.marks = marks

    def display_info(self):

        print("\n----- STUDENT INFO -----")
        print("Name :", self.name)
        print("Age :", self.age)
        print("Marks :", self.marks)

    def calculate_grade(self):

        if self.marks >= 90:
            return "A"

        elif self.marks >= 75:
            return "B"

        elif self.marks >= 50:
            return "C"

        else:
            return "Fail"

    def check_result(self):

        if self.marks >= 40:
            return "Pass"

        return "Fail"
    def is_topper(self):
        if self.marks >=95:
            return "Topper"
        elif self.marks >= 90:
            return "Good Student"
        elif self.marks >=50:
            return "Average"
        else:
            return "Not Topper"

students = []
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        try:

            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            marks = int(input("Enter Marks: "))

            student = Student(name, age, marks)

            students.append(student)

            print("Student Added Successfully!")

        except ValueError:

            print("Age and Marks must be numbers.")

    elif choice == "2":

        if len(students) == 0:

            print("No Students Found.")

        else:

            for student in students:

                student.display_info()

                print("Grade :", student.calculate_grade())

                print("Result :", student.check_result())

                print("Status :", student.is_topper())

    elif choice == "3":

        print("Program Closed.")
        break

    else:

        print("Invalid Choice")