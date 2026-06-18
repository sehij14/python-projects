import sqlite3

connection = sqlite3.connect("Day22/school_day22.db")

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

connection.commit()

# UPDATE

cursor.execute(
"""
UPDATE students
SET marks = ?
WHERE name = ?
""",
(95, "Rahul")
)

connection.commit()

# DELETE

cursor.execute(
"""
DELETE FROM students
WHERE name = ?
""",
("Aman",)
)

connection.commit()

# READ

cursor.execute(
"""
SELECT * FROM students
"""
)

students = cursor.fetchall()

print("----- STUDENT DATABASE -----")

for student in students:

    print("\nID:", student[0])

    print("Name:", student[1])

    print("Age:", student[2])

    print("Marks:", student[3])

connection.close()