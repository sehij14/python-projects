# Day7 Project
#Student Database System 

students = []

def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    marks = int(input("Enter Marks:"))

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }
    students.append(student)
    print("Student Adeed Successfully!")

def view_students():
    if len(students) == 0:
      print("No student records found.")
      return 
    print("\n---STUDENT DATABASE---")
for i, student in enumerate(students,start=1):
 print("\nStudent", i)
 print("Name :", student["name"])
 print("Age :", student["age"])
 print("Marks :", student["marks"])

while True:
   print("\n===STUDENT DATABASE SYSTEM===")
   print("1. Add Student")
   print("2. View Students")
   print("3. Exit")
   choice = input("Enter Choice: ")

   if choice == "1":
      add_student()
   elif choice == "2":
      view_students()
   elif choice == "3":
      print("Program Closed.")
      break
   else:
      print("Invalid Choice")