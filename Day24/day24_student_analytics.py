import sqlite3

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    marks INTEGER
)
""")

cursor.execute("""
INSERT INTO students(name, age, marks)
VALUES ('Rahul',18,90)
""")

cursor.execute("""
INSERT INTO students(name, age, marks)
VALUES ('Aman',19,85)
""")

cursor.execute("""
INSERT INTO students(name, age, marks)
VALUES ('Priya',18,95)
""")

cursor.execute("""
INSERT INTO students(name, age, marks)
VALUES ('Riya',20,78)
""")

cursor.execute("""
INSERT INTO students(name, age, marks)
VALUES ('Sehij', 19,99)
""")

connection.commit()

cursor.execute("SELECT COUNT(*) FROM students")
total_students = cursor.fetchone()[0]

cursor.execute("SELECT MAX(marks) FROM students")
highest_marks = cursor.fetchone()[0]

cursor.execute("SELECT MIN(marks) FROM students")
lowest_marks = cursor.fetchone()[0]

cursor.execute("SELECT AVG(marks) FROM students")
average_marks = cursor.fetchone()[0]

cursor.execute("SELECT SUM(marks) FROM students")
total_marks = cursor.fetchone()[0]

cursor.execute("""SELECT COUNT(*)
FROM students
WHERE marks >=40
""")
passed_students = cursor.fetchone()[0]

cursor.execute ("""SELECT COUNT(*)
FROM students
WHERE marks < 40
""")
failed_students = cursor.fetchone()[0]

print("----- STUDENT ANALYTICS -----")

print("Total Students:", total_students)

print("Highest Marks:", highest_marks)

print("Lowest Marks:", lowest_marks)

print("Average Marks:", average_marks)

print("Total Marks:", total_marks)

print("Passed Students:", passed_students)

print("Failed Students:", failed_students)

connection.close()