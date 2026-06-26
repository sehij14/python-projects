# Day 2 — Taking Input from the User 

**File:** "day2_user_input.py"

---

## What I built

A tiny program that asks your name, age, and city — then prints it all back as a formatted info 
card. First time the program actually talked to the user instead of just printing fixed text.

---

## How to run it

```bash
python day2_user_input.py
```

It will ask for your name, age, and city one by one. Just type and press enter.

---

## What it does

- Takes name, age, and city as input.
- Prints a USER INFORMATION with all three values.

---

## What I learned

Everything from input() comes back as a string. Even if you type a number, Python sees it as text. 
So for age I had to write " int(input("Enter your age:")) ".

That wrapping — putting int() around input() — is something I think I will use in almost every 
project now. Took me a minute to understand why it was needed but once it clicked it made total 
sense.

--- 