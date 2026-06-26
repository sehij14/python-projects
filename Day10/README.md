# Day 10 — Student Management V2 

**File used:** day10_student_management_v2.py

---

## The first time everything came together

This project is an improved version of the earlier student management programs I 
created in previous days.

In this program, I combined multiple Python concepts together to build a more 
structured Student Management System. The system can manage student records more 
efficiently using menus, conditions, loops, lists, and file handling concepts I learned 
so far.

Compared to earlier beginner projects I made, this version feels more organized and 
closer to how real management systems work at a basic level.

---

## Run it:

```bash
python day10_student_management_v2.py
```

Four options wil come and choose from them— Add Student, View Students, Save Students, 
Exit.

---

## Concepts I Used:

- lists
- dictionaries
- loops
- functions
- conditional statements
- menu-driven programming
- user input handling

---

## What each part does

**Add** — takes name and marks, stores as a dictionary in the list. Error handling 
catches non-numeric marks right there.

**View** — loops through the list with enumerate, prints each student numbered from 1.

**Save** — opens `students.txt` in write mode, writes every student's name and marks, 
one per line. Write mode means it always reflects the current list — not append, 
intentionally.

---

## My honest reflection

Looking at Day 1 (7 lines, hardcoded values) and then looking at this — 60 lines, 
multiple functions, file saving, error handling — that gap in 9 days felt significant.

Not saying that the code is perfect. But my thinking behind it got better.

---

*Day10 Done successfully*