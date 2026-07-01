# Day33/secure_student_record_handler.py

class Student:

    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks. Must be between 0 and 100.")

    def display_student(self):
        print("\nStudent ID:", self.student_id)
        print("Name:", self.name)
        print("Marks:", self.__marks)


students = []

while True:

    print("\nSTUDENT RECORD HANDLER")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        student_id = int(input("ID: "))
        name = input("Name: ")
        marks = float(input("Marks: "))

        student = Student(student_id, name, marks)
        students.append(student)

    elif choice == "2":
        for s in students:
            s.display_student()

    elif choice == "3":
        sid = int(input("Enter Student ID: "))

        for s in students:
            if s.student_id == sid:
                new_marks = float(input("Enter new marks: "))
                s.set_marks(new_marks)

    elif choice == "4":
        break

    else:
        print("Invalid choice")
        