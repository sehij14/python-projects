# Day 37 — Productivity Analytics Engine

I kept thinking — most task managers just store tasks. But what if the app actually tracked behavior and told you something about it?

That question turned into this project.

---

## What it does

Log an activity, give it a category and a productivity score, and every activity is stored with a timestamp. It pulls up the report and you get the average score, highest productivity activity, category-wise breakdown, and a performance summary.
Not a to-do list. More like a personal activity logger that thinks a little.

---

## The datetime part

```python
from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

This was new territory. Almost every real app tracks when things happen, not just what happened. By adding timestamps made this feel less like a practice project and more like something real.

---

## What the analytics actually do

Instead of just printing stored data, the report calculates your average productivity score across all activities, flags the highest activity and total score per category using a dictionary.

The category aggregation logic was the trickiest part, building totals inside a loop using a dictionary, its the same pattern as Day 36 but applied differently here.

---

## file:

`Day37/productivity_analytics_engine.py`

---

*Day 37*