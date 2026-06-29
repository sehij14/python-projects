# Day 30 — Configuration Files 

## The idea

Every project I've built has settings that are hardcoded into the Python file, such as 
school name, passing marks, max students. If these values are written directly into 
the .py file, and if any small change is required then you have to edit the actual 
code, which is risky and inflexible.

So here comes the concept of config files.

`What are configuration files:`

Configuration files are external files used to store application settings and 
preferences separately from the main program code. 

The system stores application settings inside a separate configuration file instead of 
hardcoding values directly into the program. This makes the application more flexible 
because settings can be modified without changing the actual source code.

---

## Project files:

- day30_config_system.py 
- config.json

---

## The config.json

```json
{
    "school_name": "Your School Name",
    "passing_marks": 40,
    "max_students": 100
}
```
`Try it yourself:`

You can edit this file and restart the program. The new values will load automatically.
There is no Python file needs to be touched.

---

## Running it

```bash
python "config system.py"
```
After running the program, system will show this in the output terminal:

```
===== SCHOOL CONFIGURATION SYSTEM =====
1. Show School Name
2. Show Passing Marks
3. Show Maximum Students
4. Show All Settings
5. Exit
```

---

## What I learned technically

`json.load()` reads the file and gives back a Python dictionary. After that,
`config["school_name"]` is just normal dictionary access.

Two error cases i handled — `FileNotFoundError` if the json file is missing, and `json.
JSONDecodeError` if the file exists but has a syntax error in it (like a missing comma 
or bracket). Both gives a clear message to the user instead of crashing.

---

## Reflecting on 30 days

Day 1 was 7 lines of print statements.

Day 30 is a program that reads external configuration, handles missing files, validates 
JSON format, and separates settings from code entirely.

Between those two points: input handling, conditions, loops, functions, lists,
dictionaries, file handling, error handling, OOP with 4 pillars, special methods,
modules, CSV, JSON, SQLite databases, CRUD, search, analytics, menu systems,
error handling, report export, backup systems, logging.

Every single day is built on the one before it. Looking back at Day 1 now, the difference is clearly visible.Not every day was easy but maintaining consistency throughout the journey helped me build stronger problem-solving skills and practical programming experience.

---

*Day 30 — first milestone done*  consistency over everything.