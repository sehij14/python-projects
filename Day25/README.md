## Day 25 — Menu-Driven Student Management System V3 

**Files for day25:** `day25_student_management.py` · `school_day25.db`

---

# Overview

This is the third and most complete version of the student management system.
Previous days covered individual database operations — today everything came together
into one fully interactive, menu-driven application that keeps running until you choose to exit.

In this project there is no more running the program over and over for each action. You open it once and from there you can control everything through a clean numbered menu, you can — add students, view records, search by name, update marks, or delete a student.

This is the closest thing to a real working application I've built so far.

---

# To run the program:

No external libraries needed. Only pure Python + SQLite.

Open and run the program "day25_student_management.py"

The database `school_day25.db` is created automatically on the first run.
Then no setup is needed — just run and start using it.

---

# Application Menu

Once running the program, you'll see this menu on every loop:

1. Add Student
2. View Students
3. Delete Student
4. Search Student
5. Update Marks
6. Exit


The program keeps looping back to this menu after every action until you press `6` to exit.

---

# Features & How Each One Works

## 1. Add Student
In this it asks you to enter a name, age, and marks one by one.
It then inserts the record into the database using a parameterized query and confirms with:

Student Added Successfully!


## 2. View Students
In this it fetches every row from the students table and prints them.
If the table is empty, it tells you:

No Students Found

Otherwise it prints a labelled list of all the student records.

## 3. Delete Student
This takes a student name as input and permanently removes that record from the database.
Here i used a "WHERE name = ?" clause so only the matching student is deleted. And then confirms with:

Student Deleted Successfully!


## 4. Search Student
Here it looks up a student by name using `SELECT * FROM students WHERE name = ?`
and `fetchone()` to grab a single match.

If the student is found,then prints their full record. But if the student is not found, then prints:

Student not found


## 5. Update Marks
This takes a student name and new marks as input, then runs an UPDATE query with SET marks = ? WHERE name = ? to change only that student's marks.
It then confirms with:
Marks Updated Successfully!

---

## Code Structure

day25_student_management.py
│
├── add_student()        # INSERT new record into DB
├── view_students()      # SELECT * and print all rows
├── delete_student()     # DELETE by student name
├── search_student()     # SELECT with fetchone() by name
├── update_marks()       # UPDATE marks by student name
│
└── while True loop      # Keeps the menu running until exit

---

## What I Learned from this project:

**Functions makes everything cleaner**
Each database operation lives in its own function. The menu just calls them. This was the first time I really felt the difference between code that just works and a code that's actually organized.

**while True for continuous programs**
The whole application runs inside a while True loop. It only breaks when the user picks the option 6. This is the standard pattern for any interactive CLI application that is simple but effective.

**`fetchone()` vs `fetchall()`**
When searching by name, you only expect one result — so `fetchone()` is the right call. It returns a single tuple instead of a list, and returns None if nothing matches, which makes the `if student:` check clean and become straightforward.

**Parameterized queries everywhere**
Every single query in this project uses "?" placeholders. Not one f-string or string concatenation near SQL. This is a habit I want to keep permanently.

**Committing after every write**
Every INSERT, UPDATE, and DELETE is followed by `connection.commit()`. Without it, changes exists in memory but never actually reaches the database file.

---

## Project Structure

Day25/
├── day25_student_management.py   # Full menu-driven application
└── school_day25.db               # SQLite database (auto-created on the first run)

---

## Skills This Project Demonstrates

- Building interactive CLI applications with a persistent menu loop.
- Organizing database logic into clean, reusable functions.
- Full CRUD implementation in a single cohesive application.
- Safe SQL queries using parameterized statements throughout.
- Handling empty results gracefully without crashing.

---

# *Day 25  —  Of my Python learning journey Completed *