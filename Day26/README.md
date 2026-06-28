# Day 26 — Making the Program Not Crash 

*Files Name:* `error handling.py` · `school_day26.db`

So today I finally stopped ignoring the fact that my programs crash the moment someone 
types something wrong. I've been building database stuff for a while now and every 
project so far I assumed the user would always behave.

This project is simple on the surface — enter a student's name, age, and marks,
save it to a database. But the whole point was making it handle anything that
goes wrong, cleanly.

---

### The problem I was solving

Run any of my previous database projects and type letters where numbers are expected. 
It just dies with a red traceback. It's not great but today that stops.

---

### Run it like this

```bash
python "error handling.py"
```

Try being annoying on purpose — type "abc" for age, leave things blank, type negative 
numbers. And see what happens. That's the test for my project i made today.

---

### How the error handling works

I used three blocks — `try`, `except` and `finally`. The try block attempts everything.
If something breaks, one of the except blocks catches it. Finally runs no matter what.

```python
try:
    age = int(input("Enter Age: "))
    marks = int(input("Enter Marks: "))

except ValueError:
    print("Please Enter Valid Numbers")

except sqlite3.Error:
    print("Database Error Occurred")

finally:
    connection.close()
    print("Database Connection Closed")
```

**Why I used two separate excepts?**
`ValueError` means the user typed something that can't be converted to a number.
`sqlite3.Error` means something went wrong at the database level — different problem,
different message. Catching both under one `Exception` would work but you'd lose the 
ability to tell the user what actually went wrong.

**Why finally?**
The database connection closes whether the insert succeeded or crashed midway. 
Without `finally`, a crash could leave the connection hanging open.

---

### What actually changed in how I think

Before today: my focus was on writing code and hope nothing breaks.
After today: i assume something will break and i'll handle it before it happens.

---

*Day 26 completed and further still going*