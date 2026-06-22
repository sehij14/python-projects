# Day31/Training Institute Management System

class Student:

    def __init__(self, student_id, name, course, marks):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.marks = marks

    def display_student(self):
        print("\n----- STUDENT DETAILS -----")
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Marks:", self.marks)

students = []

while True:

    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        try:
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Student Name: ")
            course = input("Enter Course Name: ")
            marks = float(input("Enter Marks: "))

            student = Student(student_id, name, course, marks)

            students.append(student)

            print("\nStudent Added Successfully!")

        except ValueError:
            print("\nInvalid Input! Please enter correct data types.")

    elif choice == "2":

        if len(students) == 0:
            print("\nNo students available.")

        else:
            print("\n========== ALL STUDENTS ==========")

            for student in students:
                student.display_student()

    elif choice == "3":
        print("\nExiting Student Management System...")
        break

    else:
        print("\nInvalid Choice! Please select valid option.")