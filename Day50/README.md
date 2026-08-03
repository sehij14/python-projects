# Day 50
# Developer Workspace Manager

---

## About

This is a terminal-based project management tool built in Python. It lets developers track their own projects with status updates, priority levels, tags and timestamps. All are stored locally in a JSON file. No database, no internet connection, no external libraries are required. Just Python's standard library doing real work.

399 lines. This is the most structured project I've written so far.
Not because of the line count but because of what's inside it. Enums, type hints, JSON persistence, lambda sorting, statistics with 'sum()' and generator expressions. Everything I've been building toward individually started showing up together in one project.

---

## Folder structure

```
Day50/
├── data/
│   └── projects.json
└── day50_developer_workspace_manager.py
```
---

## Enums — the decision that changed how this is organized

```python
class ProjectStatus(Enum):
    PLANNED = "Planned"
    IN_PROGRESS = "In Progress"
    TESTING = "Testing"
    COMPLETED = "Completed"

class ProjectPriority(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
```

Before enums I would've used plain strings "Planned", "High" scattered across the code. The problem with that is nothing stops you from typo-ing "Plannned" somewhere and the whole comparison silently fails.

Enums fix this. Status and priority values are defined once, referenced everywhere. If you type the wrong thing, Python tells you immediately instead of breaking quietly at runtime. It also makes the code read clearly 'ProjectStatus.COMPLETED' is more informative than just "Completed" in the middle of a function.

---

## Type hints throughout

```python
def load_projects() -> list:
def save_projects(projects: list) -> None:
def get_current_time() -> str:
def view_projects() -> None:
```

Every function has return type annotations. This isn't just decoration, it documents intent. A future reader (or a future me) immediately knows what each function expects and what it gives back without reading the body. It's also what IDEs use for autocomplete and error detection. Started adding these properly here and won't stop.

---

## JSON as the data layer

```python
def load_projects() -> list:
    if not PROJECT_FILE.exists():
        return []
    with PROJECT_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)

def save_projects(projects: list) -> None:
    with PROJECT_FILE.open("w", encoding="utf-8") as file:
        json.dump(projects, file, indent=4)
```

Every operation: create, update, delete loads from the file first and saves back after. The data persists between sessions without a database.'indent=4' keeps the JSON human-readable if you open it directly.

---

## Lambda sorting and statistics

Projects display sorted alphabetically by name:

```python
projects = sorted(
    load_projects(),
    key=lambda project: project["name"].lower()
)
```

Statistics use 'sum()' with generator expressions, one line per status:

```python
planned = sum(
    project["status"] == ProjectStatus.PLANNED.value
    for project in projects
)
```

'sum()' over a generator of booleans counts how many True values exist. It's clean, readable and no explicit counter variables needed.

---

## Search that covers both name and tags

```python
if (
    keyword in project["name"].lower()
    or any(
        keyword in tag.lower()
        for tag in project["tags"]
    )
):
```

One search input checks against the project name 'and' every tag in the list. The any() function short-circuits, it stops checking tags the moment it finds a match.

---

## What each project stores

```json
{
    "name": "Portfolio Site",
    "description": "Personal developer portfolio",
    "status": "In Progress",
    "priority": "High",
    "tags": ["web", "frontend"],
    "created": "2025-08-03 20:10",
    "updated": "2025-08-03 20:10"
}
```

Created and updated timestamps auto-generates. Every update refreshes the updated field so you always 
know when a project was last touched.

---

*Everything finally felt like it belonged together. enums, type hints, JSON, lambda, generator expressions. Feels less like practice, more like building something real.*