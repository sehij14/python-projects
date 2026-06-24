# Day 22 - CRUD Operations in SQLite 

**Files:** `day22_crud_system.py` · `school_day22.db`

---

## What is this?

CRUD stands for **Create, Read, Update, Delete** — the four fundamental operations of any database.
If you can do these four things, you can build almost any data-driven application.

This project is a command-line CRUD system built around a school student database. Every operation,
a real application needs — adding new records, reading them back, modifying existing ones, and
removing them — is implemented cleanly and works without breaking the database or losing the data.

---

## Project structure

Day22/
├── day22_crud_system.py      # Main script with all CRUD operations
└── school_day22.db     # SQLite database (auto-created on first run)

---

## Main Features
- Add student records
- View saved records
- Update existing records
- Delete records
- Menu-driven database system
- Persistent data storage using SQLite

---

## How to run it

No external libraries needed. Just Python.

- Open the Day 21 folder.
- Run python "day22_crud_system.py"

**What happens when you run it:**

1. It creates a school_day22.db with a students table (only if it doesn't exist) 
2. Inserts the sample student records into the database.
3. Reads and displays all the records.
4. Updates a student's grade.
5. Deletes a record by ID.
6. Displays the final state of the table.

You can modify the script to test your own inserts, updates, and deletes — everything is clearly
labeled with the comments.

---

## Technology Stack
- Python
- SQLite3
- SQL
- CRUD Operations
- VS Code

---

## What I built

**Create — Adding records**

cursor.execute("INSERT INTO students (name, age, grade) 
VALUES (?, ?, ?)", (name, age, grade))
connection.commit()

I used the parameterized queries instead of string formatting. This prevents SQL injection and is
the correct way to pass dynamic values into a query.

**Read — Fetching records**

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

fetchall() returns every row as a list of tuples. We can also use fetchone() for single lookups it is
useful when searching by ID.

**Update — Modifying existing data**

cursor.execute("UPDATE students SET marks = ? WHERE name = ?", (new_marks, student_name))
connection.commit()

The WHERE clause is critical here. Without it, you update every single row in the table.
I learned that the hard way during testing.

**Delete — Removing records**

cursor.execute("DELETE FROM students
WHERE name = ?", (student_name))
connection.commit

Same story — always filter with WHERE. Deleting without a condition, wipes the entire table.

---
# What's next

Day 23 goes deeper — search systems, filtering with WHERE clauses, and writing more advanced SQL queries to pull exactly the data you need from the database.