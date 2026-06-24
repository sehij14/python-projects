# Day 23 - Database Searching, Filtering & SQL Queries 

**Files:** `day23_search_system.py` · `school_day23.db`

---

## Overview

Inserting and retrieving all records is the easy part. The real power of a database shows up when
you can ask it specific questions — *show me students scoring above 80, or find everyone in Grade A,
or search by name without knowing the exact spelling.*

This project is a search and filter system built on a school student database. Instead of pulling
everything and filtering in Python, I pushed that logic down into SQL where it belongs — which is
faster, cleaner, and how real applications actually work.

---

## How to run it

Open the file and Run python "day23_search_system.py"

**What happens when you run it:**
1. Creates `school_day23.db` and fills it with student records.
2. Runs a series of search and filter queries.
3. Prints results for each query to the terminal — search for toppers, grade filters.
4. Shows how the same data returns different results depending on how you ask for it.

No setup needed. No external libraries. Just pure Python and SQL.

---

## What I built

# Inserting sample students

cursor.execute("""
    INSERT INTO students(name, age, marks)
    VALUES (?, ?, ?)
    """,
    ("Rahul", 18, 90)
)
connection.commit()

Added four students — Rahul (90), Aman (85), Priya (95), Riya (78) — by using parameterized queries to safely pass values into the database.

# Searching toppers with WHERE

cursor.execute("""
    SELECT * FROM students
    WHERE marks >= 90
""")
students = cursor.fetchall()

Filters and returns only the students who scored 90 or above. The filtering happens inside SQL — not in a Python loop after fetching everything.

# Finding the class topper with ORDER BY + LIMIT

cursor.execute("""
    SELECT * FROM students
    ORDER BY marks DESC
    LIMIT 1
""")
top_student = cursor.fetchone()

Sorts all students by marks in descending order and picks only the first result — the highest
scorer. Used fetchone() here since only one row is needed.

---

## Database structure

*Database:* school_day23.db
*Table:* students

| Column | Type    | Notes                       |
|--------|---------|-----------------------------|
| id     | INTEGER | Auto-increment, primary key |
| name   | TEXT    | Student full name           |
| age    | INTEGER | Student age                 |
| marks  | INTEGER | Score out of 100            |

---

## Key concepts I picked up

**Filter in SQL, not in Python**
My first instinct was to fetch all rows and loop through them in Python to find toppers. That
works — but it's wrong. If your table has 100,000 rows, you load all of them into memory just
to keep a handful. SQL filtering happens at the database level before data even reaches Python.

**ORDER BY DESC + LIMIT 1 is cleaner than sorting in Python**
Instead of fetching all rows, sorting a Python list, and grabbing index 0 — one SQL query does
it all. This is what SQL is designed for.

**fetchone() vs fetchall()**
Used fetchall() when expecting multiple results (toppers list) and fetchone() when only
one row is needed (class topper). Using the right one keeps the intention clear and avoids
unnecessary data in memory.

**Parameterized queries on every insert**
Every value going into the database uses ? placeholders — no f-strings, no .format().
This is the correct habit to build early, especially when user input is involved.

**Always commit after inserts**
Called connection.commit() after all four inserts. Without this, the data exists only in
memory for the current session and doesn't actually get saved to the .db file.

---

## Project structure

```
Day23/
├── search system.py    # Search and filter logic with SQL queries
└── school_day23.db     # SQLite database (auto-created on first run)
```

---

## Skills demonstrated

- Writing targeted SQL queries using `WHERE`, `LIMIT` and `ORDER BY`
- Filtering records based on a numeric condition (marks >= 90).
- Finding the top record using ORDER BY DESC combined with LIMIT 1.
- Safe data insertion using parameterized queries.
- Choosing between fetchone() and fetchall() based on expected results.
- Proper transaction handling with connection.commit()

---

## Up next

Day 24 moves into aggregate functions — `COUNT`, `AVG`, `SUM`, `MAX`, `MIN` — and using SQL
to generate actual analytics and summaries from the data rather than just retrieving it.

### Day 23 Completed successfully!