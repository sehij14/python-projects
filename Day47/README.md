# Day 47
## Workspace Session Tracker

This project is a lightweight Python custom context manager designed for managing workspace 
sessions safely. There's a Python feature called a context manager. You've used it every time you write 'with open(...) as file:' 

## Key Features

- `Automated Lifecycle:` Manages workspace setup and teardown automatically.
- `Guaranteed Execution:` Executes exit logic even if errors occur.
- `Built-in Logging:` Captures session start times and state transitions.
- `Pythonic Design:` Implements clean `__enter__` and `__exit__` magic methods.

---

## What a context manager actually is

When you use 'with' in Python, two things happen automatically something runs when you enter the block and something runs when you exit it, no matter what (even if an error occurs). That behavior is controlled by two special methods: `__enter__` and `__exit__`.

This project builds a 'WorkspaceSession' class that uses both:

```python
class WorkspaceSession:

    def __enter__(self):
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"START | {self.session_name} | {start_time}"
        write_log(message)
        print(f"\nSession '{self.session_name}' started.")
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # logs end time and session close
```

And using it looks like this:

```python
with WorkspaceSession(session_name):
    perform_task()
```

The moment the 'with' block is entered, '__enter__' fires, logs the start time, prints 
confirmation. The moment it exits (task done or error raised), '__exit__' fires automatically 
logs the end time. No manual open/close calls, no risk of forgetting to log the end.

---

## The three parameters in `__exit__`

```python
def __exit__(self, exception_type, exception_value, traceback):
```

These aren't just there for decoration. If an exception occurs inside the 'with' block, Python 
passes the error details through these three parameters, giving you the option to handle it 
gracefully inside '__exit__'. If everything runs fine, all three are 'None'.

This is why context managers are used for things like file handling, database connections and 
network sessions They guarantee cleanup runs regardless of what happens in between.

---

## Session logging

Every session writes two entries to `session_history.txt`:

```
START | Project Backup | 2025-07-24 20:10:44
END   | Project Backup | 2025-07-24 20:10:45
```

The log file opens in append mode each time so history accumulates across sessions. View it any 
time from the menu.

---

## Folder structure

```
Day47/
├── logs/
│   └── session_history.txt
└── day47_workspace_session_tracker.py
```

---