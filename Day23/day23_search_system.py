import sqlite3

connection = sqlite3.connect("school.db")

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

# Insert Sample Data

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

cursor.execute(
"""
INSERT INTO students(name, age, marks)
VALUES (?, ?, ?)
""",
("Riya", 20, 78)
)

connection.commit()

# Search Toppers

cursor.execute("""
SELECT * FROM students
WHERE marks >= 90
""")

students = cursor.fetchall()

print("----- TOPPERS -----")

for student in students:

    print(student)

# Top Student

cursor.execute("""
SELECT * FROM students
ORDER BY marks DESC
LIMIT 1
""")

top_student = cursor.fetchone()

print("\n----- CLASS TOPPER -----")
print(top_student)

connection.close()