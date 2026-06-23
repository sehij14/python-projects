## Day 20 - JSON Database System

I used to think databases always meant something complex like MySQL or large software systems.
But today’s project showed me that even a simple JSON file can behave like a lightweight database.

The idea behind this project was to build a small student record system using JSON file handling. Instead of storing temporary data during runtime, the program saves records permanently inside a structured ".json" file.

What made this project interesting was seeing how Python dictionaries directly connect with JSON structure. It almost felt like turning Python data into a mini database system.

---

# Files Used in This Project

day20_json_database.py
students.json

---

# Tech & Concepts Used

Technology / Concept| Purpose
Python| Core programming
JSON| Structured data storage
Dictionaries| Data organization
File Handling| Reading & writing files
OOP + Logic Building| Managing records

---

# What this Program Handles

This system can:

- store student records,
- save data into JSON format,
- read saved records,
- update information,
- and display structured student data.

Unlike earlier projects where data disappeared after closing the program, this project keeps records saved permanently inside the JSON file.

---

# Example JSON Structure

{
    "students": [
        {
            "name": "Rahul",
            "marks": 85
        }
    ]
}

---

# What Felt Different While Building This

One thing I noticed during this project was how readable JSON files are compared to normal text files.

Earlier file handling projects mainly focused on storing raw text, but JSON made the data feel much more organized and application-like.

It also became easier to imagine how APIs and real software systems exchange structured data.

---

# A Small Mistake That Helped Me Learn

At one point, I accidentally saved Python dictionary syntax incorrectly inside the JSON file, which caused formatting issues while reading the data.

That helped me understand that JSON has strict structure rules, even though it looks very similar to Python dictionaries.

---

# Why This Project Was Useful

This project acted like a bridge between:

- normal file handling,
- and actual database-style programming.

JSON is widely used in:

- APIs,
- web applications,
- configuration systems,
- and data exchange.

So this project gave me practical exposure to a format heavily used in modern software development.

---

# Running the Program

1. Open the Day 20 folder.
2. Make sure "student.json" exists in the same directory.
3. Run "day20_json_database.py"
4. The program will read/write student records using JSON.

---

# Status

Day 20 completed successfully.
