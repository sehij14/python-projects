Day 8 - Contact Book using File Handling

About the Project:

This project is based on File Handling in Python.

In this program, I created a simple Contact Book System that stores contact details 
inside a text file.

This one fixed the problem I'd been annoyed about since Day6. Data that actually 
survives after the program closes.

This project helped me understand how programs can save data permanently instead of 
losing it after the program closes.

---

File Included:

day8_contact_book.py

---

Features:

- Add new contacts.
- Save contact details in a file.
- View saved contacts.
- Store data permanently using file handling.
- Simple menu-driven system.

---

How to Run:

1. Open the Day 8 project folder.
2. Open "day8_contact_book.py"
3. Run the program.
4. Choose options from the menu.

The contact data will be saved inside the project folder using a text file:    
"contacts.txt"

First run creates the "contacts.txt" If you add contacts, close the program and run it again, they're all still there.

---

**How the saving works**

Every time you add a contact, it opens the file in append mode and writes one line — 
name, a dash, phone number. That's it.

```python
file = open(FILE_NAME, "a")
file.write(name + " - " + phone + "\n")
file.close()
```

Append mode ("a") was the key thing. I used write mode ("w") once by accident and it 
wiped everything.

---

**Reading contacts**

Opens in read mode ("r"), reads all content, prints it. Also used a `try/except 
FileNotFoundError` — if no contacts file exists yet, it shows "No Contacts Saved Yet" 
instead of crashing.

---

What I Learned:

- How files are created and managed in Python.
- Difference between read, write, and append modes.
- How data can be stored permanently.
- How real applications save records using files.

This project helped me understand the basics of persistent data storage in programming. 

--- 

Project Goal:

The goal of this project was to practice file handling and learn how Python programs 
store and retrieve data from files.

---