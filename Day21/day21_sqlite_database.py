import sqlite3

# Create Database Connection

connection = sqlite3.connect("Day21/school_day21.db")

cursor = connection.cursor()

# Create Table

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    marks INTEGER
)
""")

# Insert Records

cursor.execute(
"""
INSERT INTO students(name, age, marks)
VALUES (?, ?, ?)
""",
("Rahul", 18, 90)
)

cursor.execute(
"""
INSERT INTO students(name, age, marks)
VALUES (?, ?, ?)
""",
("Aman", 19, 85)
)

cursor.execute(
"""
INSERT INTO students(name, age, marks)
VALUES (?, ?, ?)
""",
("Priya", 18, 95)
)

# Save Changes

connection.commit()

# Read Data

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

print("----- STUDENT DATABASE -----")

for student in students:

    print("\nID:", student[0])

    print("Name:", student[1])

    print("Age:", student[2])

    print("Marks:", student[3])

connection.close()