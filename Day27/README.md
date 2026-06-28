# Day 27 — Exporting Data to CSV 

**Files for day27:** `report exporter.py` · `school_day27.db` · `students_report.csv`

---

I have been storing data in databases for a week now. Today I learned how to get it
out — not just printed to a terminal but written to an file someone could open in Excel.

This project is a menu-driven report exporter. You can add sample data, then export it. 
The result is `students_report.csv` in the folder, that is ready to open.

---

**To run:**
```bash
python "report exporter.py"
```
Pick option 1 first to add data, then select option 2 to export. And check the Day27
folder after and `students_report.csv` will be there.

---

## The two things I built in this

**Adding data with executemany()**

Instead of inserting students one by one in a loop, I learned about executemany() which 
takes a list and does all the insertions in one call.

```python code
cursor.executemany(
    "INSERT INTO students(name, age, marks) VALUES (?, ?, ?)",
    sample_students
)
```

This is cleaner and faster than looping. I will definitely use this again.

**Exporting to CSV**

```python
writer = csv.writer(file)
writer.writerow(["ID", "Name", "Age", "Marks"])  # header
for student in students:
    writer.writerow(student)
```

The header row is written first, then every database row written line by line.

---

## One thing I didn't expect while making this:

open() needs newline="" when writing CSV files on Windows. Without it you will get an 
extra blank line between every row. It took me a minute to figure out why my CSV looked 
weird at that time.

---

*Day 27 of my Python learning journey and executing it*
