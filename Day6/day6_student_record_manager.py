# Day6 Project
#Student Record Manager

students = []
def add_student():
    name = input("Enter student name:") 
    students.append(name)
    print("Student added successfully!")

def view_students():
    if len(students) == 0:
        print("No students found.")
    else:
        print("\n---STUDENT LIST---")
        for i in range(len(students)):
            print(i + 1, ".", students[i])
while True:
    print("\n===STUDENT RECORD MANAGER===")
    print("1. Add Student")
    print("2. View Students")    
    print("3. Exit")     

    choice = input("Enter your choice") 

    if choice == "1":
     add_student()
    elif choice =="2":
     view_students()
    elif choice =="3":
     print("Program Closed.")
     break

    else:
     print("Invalid Choice!")