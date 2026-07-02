# Day 35 — Resume Keyword Scanner

`Filename: day35_resume_keyword_scanner.py`

This project is a Python based *Applicant Tracking System(ATS) simulator*. It automates the process of comparing a candidate's resume against a specific job description by identifying matching skills and calculating a compatibility score.

This is a same kind of thing companies use to filter resume before recruiters even looks at them. 

---

## how it works

You paste your resume text into the scanner/terminal, the program accepts resume text from the user, scanns for predefined keywords and generates: 
matched skills, missing skills, and a verdict — strong / moderate / resume needs improvement. 
Then gives you a match score out of 100.

---

## the logic behind it

```python
score = (len(matched_skills) / len(required_skills)) * 100 
```
This core scoring is handled by a simple but effective ratio calculation.
This approach provides an objective data point for resume filtering(similar to early-stage recruitment automation)

The `.lower()` on the resume input was important too — without it, "Python" and "python" would count as different things and the whole match would break.

---

## Skills being checked in the scanner:

python · sql · git · communication · problem solving · oop · teamwork · debugging

---

# what I understood today

While building this project,I wanted to understand how keyword based filtering systems work internally. Even though real ATS software is much more advanced, but this helped me understand the core logic behind it.
Also text processing doesn't have to be complicated to be useful.

The concepts I practiced for this project was string processing, text normalization, loops,conditional logic, list handling, scoring systems, text analysis thinking.

This also made me look at my own resume differently.

---

day 35 — writing code that reads resumes while still building mine.