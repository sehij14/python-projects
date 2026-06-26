# Day 4 — Number Analyzer System 

*File Included:* day4_number_analyzer.py

---

## About the project

In this project, I created a simple Number Analyzer program that takes multiple numbers from the 
user and analyzes them using conditions and loops. A program that asks how many numbers you want to 
analyze, takes  them one by one, and counts how many were even, odd, positive, and negative. Prints 
a summary at the end.

---

## How to run it:

```bash
python day4_number_analyzer.py
```

Enter how many numbers you want to check, then type each one when says to.

---

## Features:

The program can:

- count even numbers
- count odd numbers
- count positive numbers
- count negative numbers

---

## What this program does

- It asks how many numbers to analyze first.
- Then loops through each number using for i in range(n)
- After that tracks four counters — even, odd, positive and negative.
- Prints a result summary when done.

---

## What I learned

This was my first proper use of a for loop combined with range(). The loop runs exactly as many 
times as the user specifies which made it feel dynamic for the first time.

Counters were also new foe me, starting a variable at 0 and adding 1 each time a condition is met
eg: even_count += 1  

One thing I noticed: a number can be both positive and even at the same time, so both counters 
update for the same number. The checks are independent ofeach other. 

---