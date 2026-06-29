# Day 28 

## Database Backup and Restore

**Project files :** `day28_backup_system.py` · `school_day28.db` · `school_backup_1.db`

---

## My Overview:

This project is focused on building a backup and restore system for SQLite database 
using python.

What if the database file gets corrupted or deleted? You'd lose everything. So I built 
a backup system. You can create numbered backups and restore any of them back. All from 
a terminal menu.

The main objective was to understand how database backups are created, stored, and 
restored to protect important records from accidental loss or corruption. The system 
works with an SQLite database and automatically creates backup copies that can later be 
restored when needed.

---

## Technology Stack

- Python
- SQLite3
- File Handling
- Database Management
- VS Code
- Github

---

## Core Features of my project:

- Create database backups
- Restore backup databases
- Copy database records safely
- Handle database file operations
- Maintain duplicate backup copies

---

## Concepts Used

- SQLite database handling
- backup and restore logic
- database copying
- exception handling
- database management workflows

---

### You can run this by

```bash
python "backup system.py"
```
It will show this in the terminal:
```
===== DATABASE BACKUP SYSTEM =====
1. Create Backup
2. Restore Backup  
3. Exit
```

Creating a backup: enter a number — say 1 — and it saves a copy as
`school_backup_1.db`. Enter 2 and it saves `school_backup_2.db`. And so on.

Restoring: enter the backup number you want to restore and it copies that file back
over the main database.

---

## shutil — a module I didn't know existed

The entire backup and restore logic is one line each:

```python
# backup
shutil.copy("Day28/school_day28.db", backup_name)

# restore  
shutil.copy(backup_name, "Day28/school_day28.db")
```

`shutil` handles file copying. It comes built into Python, no installation needed for 
this. Backup is just copying the file somewhere. Restore is copying it back.

The backup filename is built dynamically:
```python
backup_name = f"Day28/school_backup_{backup_number}.db"
```

So you can have as many numbered backups as you want.

---

## Error handling i used for this:

- `FileNotFoundError` — if the database or backup file doesn't exist.
- `ValueError` — if you type letters instead of a number for the backup number.

Both were things I tested on purpose after Day 26's lesson about not assuming the user 
will behave.

---

## Why This Project Matters

Backup systems are extremely important in software applications because databases can 
sometimes:
- become corrupted,
- get deleted accidentally,
- or lose important records.
This project helped me understand how applications protect data using backup strategies 
and recovery systems.
It also introduced the importance of maintaining data reliability in database-driven 
programs.

---

### Status:

day 28 completed.