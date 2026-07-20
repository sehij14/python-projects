# Day 45 — LogStream Inspector

Felt like the right time to build something that deals with logs because logs are how you understand what's happening inside a running system.

---

## What LogStream Inspector does

It reads an application log file line by line, lets you filter by log level (INFO, WARNING, ERROR), search by keyword, save filtered results to separate files, and view statistics across the full log.

The interesting part is not the menu, it's how the log file gets readed.

---

## Generators — the concept this day was built around

```python
def log_generator():
    with LOG_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()
```

Instead of reading the entire file into memory at once, `log_generator()` yields one line at a time. Every function that needs log data like `display_logs()`, `filter_logs()`, `show_statistics()`, `search_logs()` calls this generator and processes lines one by one.

For a small log file this doesn't matter that much. But the moment that file is 500MB of server logs, loading everything into a list first would crash or choke. Generators solve that, they don't care how big the file is because they never hold more than one line at a time.

That's the real reason the generators exist. Today this project made that concrete.

---

## Filtering logic

```python
def filter_logs(level):
    filtered_logs = []
    for log in log_generator():
        if log.startswith(level.upper()):
            filtered_logs.append(log)
    return filtered_logs
```

Each log line starts with its level `INFO`, `WARNING`, or `ERROR`. `startswith()` checks the beginning of the string, which is faster and more reliable than searching the whole line. Filtered results get saved to their own `.txt` file inside the `filtered_logs/` folder.

---

## Statistics output

```python
for level in counts:
    if log.startswith(level):
        counts[level] += 1
```

One pass through the generator, counting every log level simultaneously into a dictionary. No second read of the file, no extra loops. Efficient by default because the generator pattern forces you to think about single-pass processing.

---

## Log levels: what they actually mean

Most real applications use at least three levels:

- `INFO` — normal operations, things that happened as expected
- `WARNING` — something unusual but not breaking
- `ERROR` — something failed and needs attention

Filtering by level is how engineers triage problems. You don't read every log line you filter to `ERROR` first, then `WARNING`, and only look at `INFO` when you need the full picture.

This project does exactly that workflow.

---

## Folder structure

```
Day45/
├── logs/
│   └── application.log
├── filtered_logs/
│   ├── info_logs.txt
│   ├── warning_logs.txt
│   └── error_logs.txt
└── day45_logstream_inspector.py
```

---

*Day 45  I learned generators today. Turns out reading a file line by line is smarter than reading it all at once.*