import sqlite3

connection = sqlite3.connect("Day25/school_day25.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    marks INTEGER
)
""")

connection.commit()

def add_student():

    name = input("Enter Name: ")

    age = int(input("Enter Age: "))

    marks = int(input("Enter Marks: "))

    cursor.execute(
    """
    INSERT INTO students(name, age, marks)
    VALUES (?, ?, ?)
    """,
    (name, age, marks)
    )

    connection.commit()

    print("Student Added Successfully!")


def view_students():

    cursor.execute("""
    SELECT * FROM students
    """)

    students = cursor.fetchall()
    if len(students) == 0:
        print("\nNo Students Found")
    else:
        print("\n----- STUDENTS -----")

        for student in students:

          print(student)


def delete_student():

    name = input("Enter Student Name: ")

    cursor.execute(
    """
    DELETE FROM students
    WHERE name = ?
    """,
    (name,)
    )

    connection.commit()

    print("Student Deleted Successfully!")

def search_student():

    name = input("Enter Student Name:")

    cursor.execute(
    """
    SELECT * FROM students
    WHERE name = ?
    """,
    (name,)
    )
    student = cursor.fetchone()

    if student:
        print("\nID:", student[0])
        print("Name:", student[1])
        print("Age:", student[2])
        print("Marks:", student[3])

    else:
        print("Student not found")

def update_marks():

    name = input("Enter Student Name:")
    new_marks = int(input("Enter new marks:"))
    cursor.execute(
    """
    UPDATE students
    SET marks = ?
    WHERE name = ?
    """,
    (new_marks, name)
    )
    connection.commit()

    print("Marks Updated Successfullly!")

while True:

    print("\n1. Add Student")

    print("2. View Students")

    print("3. Delete Student")

    print("4. Search Student")

    print("5. Update Marks")

    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        add_student()

    elif choice == "2":

        view_students()

    elif choice == "3":

        delete_student()

    elif choice == "4":

        search_student()

    elif choice == "5":

        update_marks()

    elif choice == "6":

        print("Program Closed")

        break

    else:

        print("Invalid Choice")

connection.close()