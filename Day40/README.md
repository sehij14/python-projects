# Day 40 — Password Strength Analyzer

40 days in. Today it felt like a good checkpoint project.

I built a password analyzer that checks how secure a password actually is _ not just length, but uppercase, lowercase, numbers, special characters also. It gives a score out of 5 and tells you exactly what's missing.

---

## First real use of regex

This project introduced me to the `re` module properly.

```python
if re.search(r"[A-Z]", password):
    score += 1
```

Each `re.search()` call scans the password for a specific pattern. uppercase letters, lowercase, digits, special characters — each one is a separate check, each one adds to the score. It's a clean way to validate string patterns without writing a loop for every character.

Before this I would've tried to do it manually with loops, but regex makes it one line.

---

## scoring logic

| Score | Strength |
|-------|----------|
| 5/5 | Very Strong |
| 4/5 | Strong |
| 3/5 | Moderate |
| 0–2/5 | Weak |

every failed check adds a specific improvement suggestion to a feedback list. so you don't just get "weak" and you get told exactly why.

---

## History tracking

Analyzed passwords get stored in a list of dictionaries — password, score, strength. You can also view the full session history anytime. Nothing is saved to a file yet, but the structure is already thinking in that direction.

---

## Why this one matters

Password validation is everywhere. In login forms, sign-up flows, security tools they all run some version of this logic. Using regex to do it properly instead of brute-forcing character check.

---

## Future features I may explore

I will add *password generator*, *breached pass detection*, *common password blacklist* to my project. will also make a *GUI version*.

*Day 40 *