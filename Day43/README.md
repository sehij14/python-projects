# Day 43
# Smart XML Configuration Manager

This was my first time working with XML properly. I know that there are many uses for XML 
files like in Android projects, config files or various tools but never actually read or 
wrote one through code.

---

## What this project does

This project is all about working with an XML file that keeps track of application settings. You can add a setting, update it, delete it, search, view statistics, back it up with a timestamp, and restore the latest backup when needed. This makes for nine menu options, all working on a real .xml file.

The XML file it manages looks like this:

```xml
<?xml version='1.0' encoding='utf-8'?>
<settings>
    <setting key="theme">dark</setting>
    <setting key="language">english</setting>
</settings>
```

It has a clean structure. Every setting is a `<setting>` element with a `key` attribute and a text value inside.

---

## xml.etree — what I actually learned from this

```python
from xml.etree import ElementTree as ET

tree = ET.parse(XML_FILE)
root = tree.getroot()

for setting in root.findall("setting"):
    if setting.get("key") == key:
        setting.text = new_value
        save_tree(tree)
```

`ET.parse()` loads the XML file into a tree structure in memory. `getroot()` gives you the top-level element. `findall("setting")` returns every child element with that tag. `setting.get("key")` reads the attribute. `setting.text` is the value between the tags.

The whole thing feels like navigating a structured document which is exactly what XML is. once that clicked to my mind, everything else made sense to me.

---

## Backup and Restore

```python
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_name = f"app_settings_backup_{timestamp}.xml"
shutil.copy2(XML_FILE, destination)
```

every backup gets a unique name based on the exact time it was created. `shutil.copy2()` handles the actual file copy. restoring is to find the most recent backup:

```python
latest_backup = sorted(BACKUP_FOLDER.glob("*.xml"))[-1]
shutil.copy2(latest_backup, XML_FILE)
```

`glob("*.xml")` finds all backup files, `sorted()` orders them alphabetically and since the timestamp format is year-first, alphabetical order is the same as chronological order. `[-1]` grabs the last one. There is no date parsing needed.

---

## Duplicate check before adding

```python
def setting_exists(root, key):
    for setting in root.findall("setting"):
        if setting.get("key") == key:
            return True
    return False
```

This small function serves an important purpose. before adding any setting it checks if that key already exists. without this, you would end up with duplicate keys in the XML and no reliable way to know which one is the real value. I am starting to think about Defensive programming automatically now.

---

## Folder structure

```
Day43/
├── configurations/
│   └── app_settings.xml
├── backups/
│   └── app_settings_backup_YYYY-MM-DD_HH-MM-SS.xml
└── day43_smart_xml_configuration_manager.py
```

both folders get created automatically on the first run.

---

## What this connects to in the real world

XML configuration files are everywhere in Android AndroidManifest.xml, Maven pom.xml, .NET app configs, VS Code extension settings. the pattern this project follows that is load tree, find element, modify, save is the same pattern used in real tools that manage these files programmatically.

253 lines. This is the most structured project so far in terms of how the functions are 
organized, each one does exactly one thing, and main() just calls them based on menu input. That 
separation is something I want to keep doing going forward.

---