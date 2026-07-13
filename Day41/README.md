# Day 41 — Smart Notes CLI

This is the most complete project I've built so far.

Not just "add and view" this one actually reads and writes real `.md` files to disk, searches through them, filters by tags, and tracks statistics. It's a working notes system you can actually use from the terminal.

---

## What it does

There are eight options in the menu:

- **Create Note** — title, tags, content. saves as a `.md` file inside a `notes/` folder.
- **View All Notes** — lists every note file found in the folder.
- **View Note** — opens and displays a specific note's full content.
- **Search Notes** — keyword search that reads through every note file and returns matches.
- **Search by Tag** — finds notes that contain a specific tag.
- **Delete Note** — confirms before removing a file permanently.
- **Statistics** — tells total notes, total tags, most used tag.
- **Exit**

---

## The file system part

```python
NOTES_FOLDER = Path("Day41") / "notes"
NOTES_FOLDER.mkdir(parents=True, exist_ok=True)
```

using `pathlib.Path` instead of raw string paths was cleaner, cross-platform, and `exist_ok=True` means it won't crash if the folder already exists. These are the small details but it's the right way to handle it.

notes are saved as actual `.md` files with this structure:

```
Note Title

Tags: python, learning, cli

note content goes here...
```

---

## Filename sanitization

```python
def sanitize_filename(title):
    filename = title.strip().lower()
    filename = filename.replace(" ", "_")
    safe_name = ""
    for character in filename:
        if character.isalnum() or character in ("_", "."):
            safe_name += character
    return safe_name + ".md"
```

this strips out any characters that would break a filename like special characters, symbols, anything that isn't alphanumeric or an underscore. so a note titled `My Notes! (2026)` becomes `my_notes_2026.md` on disk. I had to think about this one properly.

---

## Tag search logic

This was the most involved part. To search by tag, the program reads every `.md` file, splits it into lines, finds line 3 (where tags are stored), parses the comma-separated values, strips and lowercases each one, then checks if the searched tag is in that list.

```python
tag_line = lines[2]
if tag_line.lower().startswith("tags:"):
    tags = [
        item.strip().lower()
        for item in tag_line[5:].split(",")
        if item.strip()
    ]
```

This list comprehension does the parsing and cleaning in one go. It's the kind of thing where you understand why Python makes this easy once you've tried doing it the long way first.

---

## Statistics

```python
most_used = max(tag_counter, key=tag_counter.get)
```

same `max()` with key pattern from Day 36 but this time applied to tags across all notes. the program reads every file, counts every tag, and surfaces the one that appears the most.

---

## Why this one feels different

Every previous project stored data in a list and lost it when the program closed. This one actually persists the notes are real files sitting in a folder.  You closes the program, reopens it and the notes are still there.

That gap between "running in memory" and "stored on disk" is a big one. Crossed it today.

---

## File Structure:

```
Day41/
├── notes/          ← gets created automatically
└── day41_smart_notes_cli.py
```

---

*Day 41  built something I'd actually use.*