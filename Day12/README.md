# Day 12 — Student Management using OOP

File name : day12_student_management_oop.py

---

I rebuilt the student management system from day10 using OOP(Object Oriented 
Programming). While it looks the same to the user but now each student is a proper 
object with its own methods.

**How you can run it:**

```bash
python day12_student_management_oop.py
```

---

The Student class has four methods this time. Not just display — it can do 
calculate its own grade, check its own result, and even decide if it's a topper.

```
student.display_info()      → name, age, marks
student.calculate_grade()   → A / B / C / Fail
student.check_result()      → Pass / Fail
student.is_topper()         → Topper / Good Student / Average / Not Topper
```

---

**The is_topper() method** was my own addition. There are four tiers — Topper at 95+,
Good Student at 90+, Average at 50+, Not Topper below that. Makes the output
more interesting than just pass/fail.

I also used **Error handling** that catches ValueError if someone types text for age or 
marks.

---

Example Output

===== STUDENT MANAGEMENT SYSTEM =====

1. Add Student
2. View Students
3. Search Student
4. Exit

Enter Choice: 1

Enter Student Name: Rahul
Enter Roll Number: 101

Student Added Successfully

---

Project Goal:

The goal of this project was to strengthen my understanding of Object-Oriented 
Programming by building a structured student management application using multiple 
objects and methods.

---

Comparing this to Day 10 (same program, no OOP) — the OOP version is longer.
But each part is easier to understand and change on its own. Initially, it was slightly 
confusing to combine lists with objects, but after practicing object handling and 
method calls, the overall structure became much clearer.

---
