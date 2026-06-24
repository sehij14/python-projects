# Day 21 - Introduction to SQLite Databases

**Files:** "sqlite database.py" · "school_day21.db"

---

## About this project?

This is where I stopped storing data in Python lists and actually started using a real database.
SQLite is a lightweight database that saves everything into a single `.db` file — and the best part
is that it comes built into Python, so no installations needed.

I built a simple school student database and learned how the whole connection → query → save cycle works.

---

## How to run it: 

Make sure you have Python installed (SQLite comes with it).

- Open the Day 21 folder.
- Run python "day21_sqlite_database.py"
- When you run it, it will:
   Create the school_day21.db file automatically (if it doesn't exist)
- Set up a students table inside it
- Insert some sample student records
- Fetch and print them to the terminal
- If you run it a second time, it won't crash or duplicate the table — I used
CREATE TABLE IF NOT EXISTS specifically for that.

## What I learned

- Connecting to a database
sqlite3.connect('school_day21.db') opens the database. If the file doesn't exist, SQLite just creates it.
Simple, but it felt like a big deal the first time I saw a .db file appear out of nowhere.

- The cursor
You don't run queries directly on the connection — you need a cursor object to do that.
Think of the connection as the door to the database, and the cursor as the hand that does the actual work inside.

- Committing changes
When you insert data, it doesn't actually save until you call conn.commit().
Skipped this once and spent a good while wondering why my data kept disappearing.

- Closing the connection
Always close the database when you're done with it. I put it in a finally block so it closes
even if something goes wrong mid-way.

## Database Structure

Database: school_day21.db
Table: students


| Column | Type    | Notes                        |
|--------|---------|------------------------------|
| id     | INTEGER | Auto-increments, primary key |
| name   | TEXT    | Student's full name          |
| age    | INTEGER | Student's age                |
| marks  | INTEGER | e.g. 85, 90, 96              |

## Honest thoughts
The workflow — connect, create cursor, execute query, commit, close — felt like a lot of steps just
to store a few names. But once I understood why each step exists, it started making sense.
This structure is what makes databases reliable, especially when things go wrong mid-operation.

## What's next
Day 22 will cover full CRUD operations — Create, Read, Update, Delete. Time to actually do things
with the database instead of just setting it up.

## Day 21 completed!
