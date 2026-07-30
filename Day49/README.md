# Day 49 - Workflow Status Manager

## Project Overview

The Workflow Status Manager is a command-line Python application that helps manage workflows or tasks by tracking their current status. It allows users to create new workflows, view existing workflows, and update their status through an interactive menu.

This project stores workflow data in a text file, making it simple while introducing concepts commonly used in real-world applications such as file handling, enums, modular functions and structured project organization.

---

## Features:

- It creates new workflows.
- It will automatically assign pending status to the new workflows.
- It can view all saved workflows and can update workflow status.
- Four workflow states:
  - Pending
  - In Progress
  - Completed
  - Cancelled
- It stores data permanently in a text file.
- It has clean and modular function-based design

---

## Concepts Used

These concepts are used in this project:

Python Functions, enum Class, file Handling, pathlib module, Reading and Writing Text Files, lists, String operations, Exception handling, type hints, Menu-Driven programming.

---

## Project Structure

```
Day49/
│
├── day49_workflow_status_manager.py
│
└── data/
    └── workflows.txt
```

---

## How It Works

1. Start the program(day49_workflow_status_manager.py)
2. Choose an option from the main menu.
3. Create a workflow by entering its name.
4. The workflow is saved with Pending status.
5. View all workflows whenever needed.
6. Select any workflow to update its status.
7. All changes are automatically saved to the text file.

---

## Menu options

```
====== WORKFLOW STATUS MANAGER ======

1. Create Workflow
2. View Workflows
3. Update Workflow Status
4. Exit
```

---

## Sample Output:

``` 
====== WORKFLOW STATUS MANAGER ======
1. Create Workflow
2. View Workflows
3. Update Workflow Status
4. Exit
Enter your choice: 1

Enter workflow name: Client Website

Workflow created successfully.

1. Client Website | Pending

Enter your choice: 3

Choose New Status
1. Pending
2. In Progress
3. Completed
4. Cancelled

Enter your choice: 2
Workflow updated successfully.

1. Client Website | In Progress
```
--- 

This project focuses on building practical command line applications using clean, modular and maintainable Python code.  

Day49: Done