import sqlite3
import csv

connection = sqlite3.connect("Day27/school_day27.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    marks INTEGER
)
""")

connection.commit()

def add_sample_data():
    cursor.execute("""
    SELECT COUNT(*) FROM students
    """)

    total = cursor.fetchone()[0]
    if total == 0:
        sample_students = [
            ("Rahul", 19, 90),
            ("Aman", 18, 85),
            ("Priya", 18, 95),
            ("Riya", 20, 78)
        ]
        cursor.executemany(
            """
            INSERT INTO students(name, age, marks)
            VALUES (?, ?, ?)
            """,
            sample_students
            )
        connection.commit()
        print("Sample Student data added!")

def export_report():
    try:
        cursor.execute("""
        SELECT * FROM students
        """)
        students = cursor.fetchall()
        
        file = open(
           "Day27/students_report.csv",
           "w",
           newline=""
        )

        writer = csv.writer(file)

        writer.writerow(
           ["ID", "Name", "Age", "Marks"]
        )

        for student in students:
    
            writer.writerow(student)

        file.close()
        print("\nReport exported successfully!")
        print(
            "File Name: students_report.csv"
        )

    except Exception as error:
        print("Error", error)

while True:
    print("\n===STUDENT REPORT EXPORTER===")
    print("1. Add Sample Data")
    print("2. Export Student Report")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        add_sample_data()

    elif choice == "2":

        export_report()

    elif choice == "3":

        print(
            "Program Closed"
        )

        break

    else:

        print(
            "Invalid Choice"
        )

connection.close()