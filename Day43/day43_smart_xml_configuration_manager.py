from pathlib import Path
from datetime import datetime
from xml.etree import ElementTree as ET
import shutil


BASE_FOLDER = Path("Day43")
CONFIG_FOLDER = BASE_FOLDER / "configurations"
BACKUP_FOLDER = BASE_FOLDER / "backups"
XML_FILE = CONFIG_FOLDER / "app_settings.xml"


def create_required_folders():
    CONFIG_FOLDER.mkdir(parents=True, exist_ok=True)
    BACKUP_FOLDER.mkdir(parents=True, exist_ok=True)


def create_xml_file():
    if XML_FILE.exists():
        return

    root = ET.Element("settings")

    tree = ET.ElementTree(root)

    tree.write(
        XML_FILE,
        encoding="utf-8",
        xml_declaration=True
    )


def load_tree():
    return ET.parse(XML_FILE)


def save_tree(tree):
    tree.write(
        XML_FILE,
        encoding="utf-8",
        xml_declaration=True
    )


def backup_xml():
    if not XML_FILE.exists():
        return

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    backup_name = f"app_settings_backup_{timestamp}.xml"

    destination = BACKUP_FOLDER / backup_name

    shutil.copy2(XML_FILE, destination)


def setting_exists(root, key):
    for setting in root.findall("setting"):
        if setting.get("key") == key:
            return True

    return False


def add_setting():
    tree = load_tree()
    root = tree.getroot()

    key = input("Setting key: ").strip()

    if not key:
        print("Key cannot be empty.\n")
        return

    if setting_exists(root, key):
        print("Setting already exists.\n")
        return

    value = input("Setting value: ").strip()

    setting = ET.SubElement(root, "setting")

    setting.set("key", key)

    setting.text = value

    save_tree(tree)

    print("Setting added successfully.\n")


def list_settings():
    tree = load_tree()
    root = tree.getroot()

    settings = root.findall("setting")

    if not settings:
        print("No settings found.\n")
        return

    print("\nApplication Settings\n")

    for index, setting in enumerate(settings, start=1):
        print(
            f"{index}. "
            f"{setting.get('key')} "
            f"= {setting.text}"
        )

    print()

def update_setting():
    tree = load_tree()
    root = tree.getroot()

    key = input("Enter setting key to update: ").strip()

    for setting in root.findall("setting"):
        if setting.get("key") == key:
            new_value = input("Enter new value: ").strip()

            setting.text = new_value

            save_tree(tree)

            print("Setting updated successfully.\n")
            return

    print("Setting not found.\n")


def delete_setting():
    tree = load_tree()
    root = tree.getroot()

    key = input("Enter setting key to delete: ").strip()

    for setting in root.findall("setting"):
        if setting.get("key") == key:
            root.remove(setting)

            save_tree(tree)

            print("Setting deleted successfully.\n")
            return

    print("Setting not found.\n")


def search_setting():
    tree = load_tree()
    root = tree.getroot()

    key = input("Enter setting key to search: ").strip()

    for setting in root.findall("setting"):
        if setting.get("key") == key:
            print("\nSetting Found")
            print("----------------------")
            print(f"Key   : {setting.get('key')}")
            print(f"Value : {setting.text}\n")
            return

    print("Setting not found.\n")


def show_statistics():
    tree = load_tree()
    root = tree.getroot()

    settings = root.findall("setting")

    print("\nConfiguration Statistics")
    print("------------------------------")
    print(f"Total Settings : {len(settings)}")
    print()


def restore_latest_backup():
    backups = sorted(BACKUP_FOLDER.glob("*.xml"))

    if not backups:
        print("No backups found.\n")
        return

    latest_backup = backups[-1]

    shutil.copy2(latest_backup, XML_FILE)

    print("Latest backup restored successfully.\n")

    