# Day 42 — Smart Project Archiver

I came into today knowing I would be working with zip files. But left with new understanding that compression isn't magic, it's math you can measure.

---

## What this project does

It manages project folders and archives them into `.zip` files. You can create an archive, peek inside it, check its compression stats, extract it back out, or delete it. It covers the full archive lifecycle from one terminal menu.

Sample projects  are generated automatically on first run, providing actual data to work with immediately.

---

## The part I spent the most time understanding

```python
with ZipFile(zip_file, "w", compression=ZIP_DEFLATED) as archive:
    for file in project.rglob("*"):
        if file.is_file():
            relative_path = file.relative_to(project)
            archive.write(file, arcname=relative_path)
```

`rglob("*")` walks through every file in the folder recursively, including subfolders, nested files and everything.

`file.relative_to(project)` removes the full system path keeping only the path inside the project folder. Without this, the zip file would contain absolute paths like `/home/user/Day42/projects/Project_A/notes.txt` instead of just `notes.txt`. That line is what that makes the archive portable.

`ZIP_DEFLATED` is the compression algorithm used by the most zip tools use by default.

---

## Compression Statistics

I hadn't planned to care about this feature, butit turned out to be the most interesting part.

```python
for item in archive.infolist():
    total_original_size += item.file_size
    total_compressed_size += item.compress_size

saved = total_original_size - total_compressed_size
percentage = (saved / total_original_size) * 100
```

`infolist()` returns the metadata for every file inside the zip, including both the original and compressed sizes. By subtracting one from the other, you can see exactly how much space was saved and by what percentage.

seeing actual numbers come out of this "compressed by 42%" made compression feel real instead of abstract.

---

## What pathlib is doing throughout

Almost every file operation in this project goes through `pathlib.Path` instead of raw strings:

```python
PROJECTS_FOLDER = BASE_FOLDER / "projects"
destination = EXTRACTED_FOLDER / project_name
destination.mkdir(parents=True, exist_ok=True)
```

the `/` operator builds paths. `mkdir(parents=True, exist_ok=True)` creates the full folder chain without crashing if it already exists. `file.unlink()` deletes a file. It's clean and readable, and it works the same on Windows, Mac and Linux without changing the code.

---

## Folder structure

```
Day42/
├── projects/
│   ├── Project_A/
│   │   ├── notes.txt
│   │   ├── report.md
│   │   └── config.json
│   └── Project_B/
│       ├── data.txt
│       └── summary.md
├── archives/         ← .zip files land here
├── extracted/        ← extracted content lands here
└── day42_smart_project_archiver.py
```

all three output folders get created automatically on first run. nothing needs to be set up manually.

---

## What clicked today

Day 41 was about persisting data to files. Day 42 is about managing those files at a higher level packaging them, compressing them, inspecting them and moving them around.

These two days in sequence actually make sense. reading and writing files then archiving and 
managing collections of files. This progression feels real.

---

*day 42 -- zip files, compression math, recursive folder walking.*
