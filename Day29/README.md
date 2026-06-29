# Day 29 -- Logging System

**logging system.py + activity_log.txt**

---

Every time I've run any of my programs, things happen and then disappear.
A student gets added — printed to terminal, gone when closed. An error occurs —
shows up, gone when closed. There is no record and no history.

Today I learned about this and fixed that. Not for the database, just for the activity 
itself. Every action the user takes now gets written to `activity_log.txt` with
a timestamp permanently.

---

run it:
```bash
python "logging system.py"
```

After using it, open `activity_log.txt` and you'll see every action that happened 
what was done and exactly when.

---

### The logging function

This is the whole thing:

```python
from datetime import datetime

def write_log(message):
    file = open("Day29/activity_log.txt", "a")
    file.write(f"{datetime.now()} - {message}\n")
    file.close()
```

It's only four lines. Every action in the program calls this with a message and it
gets written to the file with a timestamp.

`"a"` is append mode — it adds to the end of the file without wiping what's already 
there. If I used `"w"` it would overwrite the log every time and the whole point would be gone.

---

### What the log looks like

After this program, I got to know that a log looks like this:

```
2024-01-15 14:32:01 - Student Rahul Added
2024-01-15 14:32:45 - Student Aman Deleted
2024-01-15 14:33:12 - Backup Created
2024-01-15 14:33:20 - Program Closed
```

---

### Features

- It record user activities
- Store logs in a text file
- Track application events
- Maintain activity history
- Append new logs automatically

---

### Why this matters more than it seems

Logging is how you figure out what happened when something goes wrong. If a student 
record disappeared and you don't have any logs, you have no idea when or how the 
student record disappers, but With logs you can trace exactly what happened and when.

---

### Menu options 

1. Add Student
2. Delete Student
3. Create Backup
4. Exit

Each one logs its action before or after executing the program.

---

## This is all about day29 of my Python learning journey
