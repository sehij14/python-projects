# Day 24 — SQL Aggregate Functions & Database Analytics 

**Files:** `student analytics.py` · `school_day24.db`

---

# About My Project

Before today I could store and fetch data from a database — but I couldn't actually analyze it.
Today I learned how to make SQLite to do the math for me.

This program creates a student database, fills it with 5 students, and then runs a full analytics
report using SQL aggregate functions — total count, highest marks, lowest marks, average, sum,
and how many students passed or failed. Everything calculated directly in SQL, no Python math involved.

---

# How To Run

Here no installations needed. SQLite comes built into Python.

Open and run python - "student analytics.py"

**When you run it:**
1. It creates `school_day24.db` (if it doesn't already exist)
2. Then sets up a `students` table with `id`, `name`, `age`, and `marks`
3. Inserts 5 students — Rahul, Aman, Priya, Riya, and Sahij.
4. Runs all analytics queries.
5. Prints the full report in your terminal.

You can run it again anytime — the `CREATE TABLE IF NOT EXISTS` makes sure that it won't crash or duplicate data.

---

# Students in the Database:

| Name  | Age | Marks |
|-------|-----|-------|
| Rahul | 18  | 90    |
| Aman  | 19  | 85    |
| Priya | 18  | 95    |
| Riya  | 20  | 78    |
| Sahij | 19  | 99    |

---

# What This Project Does

This isn't just a program that runs the queries — it's a mini analytics engine. Here's what it
computes from the student database:

| Analysis | What it answers |
|---|---|
|Total student count | How many students are in the database?|
| students average marks | How are the overall students performing? |
| Highest & lowest marks | Who's at the top and bottom? |
| Total  marks | What are the total marks? |
| Passed students | How many students have passed the test? |
| Failed students | How many students have failed the test? |

Every single one of these is done with a single SQL query — no Python loops, no manual
calculations. That was the whole point of my today's topic.

---

# What The Program Calculates

Every single one of these is done with a direct SQL query — i used no loops, no Python calculations:

| Metric | SQL Used | What It Tells You |
|---|---|---|
| Total students | `COUNT(*)` | How many records exist |
| Highest marks | `MAX(marks)` | The top scorer |
| Lowest marks | `MIN(marks)` | The lowest scorer |
| Average marks | `AVG(marks)` | Overall class performance |
| Total marks | `SUM(marks)` | Combined marks of all students |
| Passed students | `COUNT(*) WHERE marks >= 40` | Students who passed |
| Failed students | `COUNT(*) WHERE marks < 40` | Students who failed |

---

# Sample Output

----- STUDENT ANALYTICS -----
Total Students:   5
Highest Marks:    99
Lowest Marks:     78
Average Marks:    89.4
Total Marks:      447
Passed Students:  5
Failed Students:  0

---

# SQL Concepts I Used

**`COUNT(*)`** — Counts all rows in the table
```sql
SELECT COUNT(*) FROM students;
```

**`MAX()` and `MIN()`** — Finds the highest and lowest value in a column

SELECT MAX(marks) FROM students;
SELECT MIN(marks) FROM students;


**`AVG()`** — Calculates the mean across all rows

SELECT AVG(marks) FROM students;

**`SUM()`** — Adds up all values in a column

SELECT SUM(marks) FROM students;

**`WHERE` with aggregate** — Filter rows before counting.

SELECT COUNT(*) FROM students WHERE marks >= 40;
SELECT COUNT(*) FROM students WHERE marks < 40;

---

# Database Structure

**Database:** `school_day24.db`
**Table:** `students`

| Column | Type    | Notes                       |
|--------|---------|-----------------------------|
| id     | INTEGER | Primary key, auto-increment |
| name   | TEXT    | Student full name           |
| age    | INTEGER | Student age                 |
| marks  | INTEGER | Marks scored out of 100     |

---

# What I Actually Learned

The biggest realization today was that I don't need to fetch all the data into Python and
then calculate things manually. SQL has these functions built in and they run directly on
the database — which is faster and much cleaner code.

fetchone()[0] was something I used a lot today. Since aggregate functions always return
a single value, fetchone() grabs that one row and [0] pulls the actual number out of
the tuple. It is a small thing but it made the code look neat.

The passed/failed split using `WHERE marks >= 40` and `WHERE marks < 40` was satisfying to
write — two simple queries and you instantly have a meaningful breakdown of the class.

---

# Project Structure

Day24/
├── day24_student_analytics.py    # Main script — analytics engine
└── school_day24.db          # Auto-generated SQLite database

---

# Skills this  project shows

- Writing SQL aggregate queries — COUNT, MAX, MIN, AVG, SUM.
- Filtering data with WHERE conditions before aggregating.
- Using `fetchone()[0]` to extract single computed values cleanly.
- Building a self-contained analytics report with zero external dependencies.
- Applying `CREATE TABLE IF NOT EXISTS` for safe, repeatable script execution.

## Day24 COMPLETED SUCCESSFULLY!