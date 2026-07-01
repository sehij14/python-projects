# Day 33 – Secure Student Record Handler

**Topic:** Encapsulation, Data Hiding, Getters & Setters

---

Today's program is like a proper upgrade from just "writing classes" to actually thinking about how data should be protected inside them.

The project is a simple secure student record handler — you can add students, view them, and update their marks. But the interesting part is how marks are stored and accessed.

---

## What I learned

Encapsulation basically means keeping data safe inside a class and only letting it be changed in controlled ways. Instead of just doing `student.marks = -50` and breaking everything, I used a private attribute `__marks` (the double underscore is Python's way of hiding it) and then wrote a `set_marks()` method that checks if the value is between 0 and 100 before accepting it.

That's the getter/setter pattern — `get_marks()` returns the value, `set_marks()` validates before setting it.

These are small thing, but it changes how you think about classes completely.

---

## Project — what it does

- It adds a new student (ID, name, marks)
- View all students.
- Update marks for a specific student by ID.
- Marks are validated means invalid values get rejected with a message.
- Runs in a loop until you choose to exit.

---

## File

`day33_secure_student_record_handler.py`

---

## Important note

The `__marks` attribute can't be directly accessed from outside the class. You have to go through `get_marks()` or `set_marks()`. 

---

## Concept recap

| Term | What it means |
|---|---|
| Encapsulation | Wrapping data + methods together in a class and restricting direct access to it. |
| Data hiding | Making attributes private with `__` underscore |
| Getter | Method that returns a private value |
| Setter | Method that validates before setting a value |

---

*Day 33 — slowly making classes actually make sense.*