# Day 21 — Introduction to  SQLite databases

**Files:** `sqlite database.py` · `school_day21.db`

---

## What I built

Before today, every time I closed my program all the data was gone. Lists, dictionaries —
all of it vanished. Today I finally learned how to actually save data using SQLite.

SQLite is a lightweight database that stores everything in a single .db file and the best part is it comes
built into Python so there's nothing to install. I created a basic school database, set up a students
table, added some records, and read them back. Small thing, but it felt like a proper step forward.

---

## How to run it:

- Open the Day 21 folder.
- Run python "day21_sqlite_database.py"
- When you run it, the program will automatically create the school_day21.db file (if it doesn't exist)
- If you run it for a second time, it won't crash or duplicate the table because I used
CREATE TABLE IF NOT EXISTS specifically for that.

That's it. There is no setup needed.

---

## What this program does

- It creates the database file and students table on the first run.
- Then inserts a few sample student records.
- Then fetches and prints all records to the terminal.
- Uses `CREATE TABLE IF NOT EXISTS` so when running it multiple times doesn't cause errors.

---

## What I learned today

The flow is to: connect → get a cursor → run your query → commit → close. Every step matters.

I forgot `conn.commit()` early on and couldn't figure out why my data kept disappearing after the program 
closed. It turns out that writes don't actually save until you explicitly commit them.
That was a frustrating 20 minutes but I won't forget it now.

I also learned that `INTEGER PRIMARY KEY` in SQLite automatically becomes an auto-incrementing ID.
Didn't expect that, but it's really convenient.

---

## What's next

Day 22 will cover full CRUD operations — Create, Read, Update, Delete. Time to actually do things
with the database instead of just setting it up.

---

*Day 21 of Python learning journey completed*