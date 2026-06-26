# Day 3 — Smart User Decision System 

File name: day3_final_project.py

---

## What I built

I built a program that takes your name, age, marks, and a number — then runs four different checks 
on them and prints all the results at once.

This was the first project that felt like it was actually doing something useful.

---

## How to run it

```bash
python day3_final_project.py
```

Enter your name, age, marks, and any number when asked and press enter.

---

## What it does

- Checks voting eligibility based on age (18+)
- Assigns a grade based on marks — A, B, C, or Fail.
- Checks if your number is even or odd.
- Checks if your number is positive, negative, or zero.
- Prints all results together at the end.

---

## What I learned

elif was the new thing today. I understood if and else but elif lets you check multiple conditions 
in a clean chain without nesting things inside each other.

I also learned that order matters a lot. In the grade check, if I put `marks >= 50` before    
`marks >= 75`, Python would match the first one for a student with 80 marks and give them a C 
instead of a B. The conditions have to go from highest to lowest.

The modulus operator "%" for even/odd was new too. number % 2 == 0 means no remainder when 
divided by 2, so it's even.

---

## Why This Day Was Important:

Today I learned how programs perform calculations using user input and operators.

This helped me understand how mathematical logic works inside applications and how values can be 
processed dynamically.

---