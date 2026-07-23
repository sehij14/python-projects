# Day 46 — Function Performance Monitor

Most Python projects I'd built until this point had no idea what was happening inside them while they ran. But this one does.

---

## The core idea

A decorator that wraps any function, times its execution, counts how many times it's been called, and logs everything to a file without touching the function itself.

```python
def performance_monitor(function):
    def wrapper(*args, **kwargs):
        function_name = function.__name__
        CALL_COUNTS[function_name] = (
            CALL_COUNTS.get(function_name, 0) + 1
        )
        start_time = perf_counter()
        function(*args, **kwargs)
        end_time = perf_counter()
        execution_time = end_time - start_time
        write_log(
            f"{function_name} | "
            f"Run #{CALL_COUNTS[function_name]} | "
            f"{execution_time:.6f} seconds"
        )
    return wrapper
```

Then using it is just this:

```python
@performance_monitor
def generate_report():
    print("Generating monthly performance report...")
```

There's no changes to the function body. The decorator handles everything around it.

---

## Why `perf_counter()` and not `time()`

`time.time()` measures wall-clock time, it can drift if the system clock changes. `time.perf_counter()` is specifically designed for measuring short durations accurately. For performance monitoring, that precision matters. Six decimal places on execution time isn't overkill it's the right tool.

---

## What gets tracked

Every decorated function logs its name, which run number it is, and how long it took. That data 
goes into `function_log.txt` in append mode so the full session history is preserved. The 
`CALL_COUNTS` dictionary holds per-function call counts in memory for the statistics view.

---

## What the menu does

| Option | Action |
|--------|--------|
| 1 | Run generate_report() |
| 2 | Run clean_temp_files() |
| 3 | Run backup_project() |
| 4 | View call statistics for all functions |
| 5 | View full execution log history |
| 6 | Exit |

Each of the three functions is decorated with @performance_monitor so every time you run one, it gets timed, counted, and logged automatically.

---

## What decorators actually are

A decorator is a function that takes another function as input and returns a modified version of it. The @ syntax is just shorthand  @performance_monitor above a function definition is exactly the same as writing `generate_report = performance_monitor(generate_report)` after it.

This pattern is used heavily in real Python frameworks. Flask uses @app.route() to register URL endpoints. Django uses decorators for authentication checks. Understanding how they work at this level not just how to use them, is what separates someone who reads documentation from someone who can write their own tooling.

---

## Folder structure

```
Day46/
├── logs/
│   └── function_log.txt
└── day46_function_performance_monitor.py
```

---

*Built a tool that watches other functions run. Decorators went from confusing syntax to something I can now write from scratch.*