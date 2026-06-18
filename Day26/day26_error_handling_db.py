import sqlite3

connection = sqlite3.connect("Day26/school_day26.db")

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

try:

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

except ValueError:

    print("Please Enter Valid Numbers")

except sqlite3.Error:

    print("Database Error Occurred")

finally:

    connection.close()

    print("Database Connection Closed")