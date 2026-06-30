# Day 31 # Training Institute Management System

**File included for day31:** `training_institute_management_system.py`

---

I built this project to dive back into Object-Oriented Programming (OOP). After spending the last 10 days focusing on databases, this was a great way to reinforce how to structure data using classes and objects in Python.

The system acts as a simple in-memory database to manage student records during a session.

Here the students are objects, they have an ID, a name, a course, and marks. You can add them through a menu and display them all. Everything lives in memory for the session.

---

## Features:

- `Student Object Modeling:` Uses OOP to represent students with attributes like ID, Name,      course, and Marks.
- `Add Students:` Capture essential details like Name, Id, Course and Marks.
- `View Records:` It generates a clean, formatted list of all students currently stired in the system.
- `Interactive Menu:` Made a simple command-line interface that makes navigation easy for the user. 
- `Data Display:` Formatted the output to view all registered students at a glance.

---

## Technologies Used:
- Python
- VS Code
- GitHub and Git

---

**How to run:**

Ensure you have Python installed, then execute the program via terminal:

```bash
python training_institute_management_system.py
```

The menu gives you three options — Add Student, Display All Students, Exit. You can dd a few students then display them to see the formatted output.

---

**What's in the Student class**

```python
class Student:
    def __init__(self, student_id, name, course, marks):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.marks = marks

    def display_student(self):
        print("----- STUDENT DETAILS -----")
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Marks:", self.marks)
```

I used the simple class, clean method. The display logic belongs to the object.

---

**The interesting part — error handling inside OOP**

Adding a student is wrapped in try/except. If you type letters for ID or marks, it catches the ValueError and asks again rather than crashing the system:

```python
try:
    student_id = int(input("Enter Student ID: "))
    marks = float(input("Enter Marks: "))
except ValueError:
    print("Invalid Input! Please enter correct data types.")
```

`float` for marksinstead of `int` so that decimal scores like 87.5 will also work.

**No database today**

All students are stored in a list `students = []` and cleared when the program closes. After 10 days of persistent SQLite storage, going back to in-memory felt noticeably limited. You add 5 students, close the program, they're all gone.

That contrast made me appreciate databases more than any explanation would have.

---

### My Process
This project was part of my Day 31 of learning Python. Moving from simple scripts to a class-based structure helped me think more about how different parts of a program interacts. 