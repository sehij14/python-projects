from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from datetime import datetime


BASE_FOLDER = Path("Day42")
PROJECTS_FOLDER = BASE_FOLDER / "projects"
ARCHIVES_FOLDER = BASE_FOLDER / "archives"
EXTRACTED_FOLDER = BASE_FOLDER / "extracted"


def create_required_folders():
    PROJECTS_FOLDER.mkdir(parents=True, exist_ok=True)
    ARCHIVES_FOLDER.mkdir(parents=True, exist_ok=True)
    EXTRACTED_FOLDER.mkdir(parents=True, exist_ok=True)


def create_sample_projects():
    samples = {
        "Project_A": {
            "notes.txt": "Meeting notes\nProject planning",
            "report.md": "# Weekly Report\nEverything is working.",
            "config.json": '{ "theme": "dark" }'
        },
        "Project_B": {
            "data.txt": "Sample dataset",
            "summary.md": "# Summary\nProject completed."
        }
    }

    for folder_name, files in samples.items():
        folder = PROJECTS_FOLDER / folder_name
        folder.mkdir(exist_ok=True)

        for filename, content in files.items():
            file_path = folder / filename

            if not file_path.exists():
                file_path.write_text(content, encoding="utf-8")


def get_project_path(project_name):
    return PROJECTS_FOLDER / project_name


def archive_path(project_name):
    return ARCHIVES_FOLDER / f"{project_name}.zip"


def list_projects():
    projects = [
        folder
        for folder in PROJECTS_FOLDER.iterdir()
        if folder.is_dir()
    ]

    if not projects:
        print("\nNo projects available.\n")
        return

    print("\nAvailable Projects\n")

    for index, folder in enumerate(projects, start=1):
        print(f"{index}. {folder.name}")

    print()


def create_archive():
    project_name = input("Enter project name: ").strip()

    project = get_project_path(project_name)

    if not project.exists():
        print("Project not found.\n")
        return

    zip_file = archive_path(project_name)

    with ZipFile(
        zip_file,
        "w",
        compression=ZIP_DEFLATED
    ) as archive:

        for file in project.rglob("*"):

            if file.is_file():

                relative_path = file.relative_to(project)

                archive.write(
                    file,
                    arcname=relative_path
                )

    print(f"\nArchive created successfully.")
    print(zip_file)
    print()

def list_archive_contents():
    project_name = input("Enter archived project name: ").strip()

    zip_file = archive_path(project_name)

    if not zip_file.exists():
        print("Archive not found.\n")
        return

    with ZipFile(zip_file, "r") as archive:
        file_names = archive.namelist()

        if not file_names:
            print("Archive is empty.\n")
            return

        print("\nFiles Inside Archive\n")

        for index, file_name in enumerate(file_names, start=1):
            print(f"{index}. {file_name}")

        print()


def show_archive_statistics():
    project_name = input("Enter archived project name: ").strip()

    zip_file = archive_path(project_name)

    if not zip_file.exists():
        print("Archive not found.\n")
        return

    with ZipFile(zip_file, "r") as archive:
        information = archive.infolist()

        total_original_size = 0
        total_compressed_size = 0

        for item in information:
            total_original_size += item.file_size
            total_compressed_size += item.compress_size

        print("\nArchive Statistics")
        print("----------------------------")
        print(f"Files               : {len(information)}")
        print(f"Original Size       : {total_original_size} bytes")
        print(f"Compressed Size     : {total_compressed_size} bytes")

        if total_original_size > 0:
            saved = total_original_size - total_compressed_size
            percentage = (saved / total_original_size) * 100

            print(f"Space Saved         : {saved} bytes")
            print(f"Compression         : {percentage:.2f}%")

        print()


def extract_archive():
    project_name = input("Enter archived project name: ").strip()

    zip_file = archive_path(project_name)

    if not zip_file.exists():
        print("Archive not found.\n")
        return

    destination = EXTRACTED_FOLDER / project_name

    destination.mkdir(parents=True, exist_ok=True)

    with ZipFile(zip_file, "r") as archive:
        archive.extractall(destination)

    print("\nArchive extracted successfully.")
    print(destination)
    print()


def delete_archive():
    project_name = input("Enter archive name to delete: ").strip()

    zip_file = archive_path(project_name)

    if not zip_file.exists():
        print("Archive not found.\n")
        return

    confirmation = input(
        "Delete this archive? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":
        zip_file.unlink()
        print("Archive deleted successfully.\n")
    else:
        print("Deletion cancelled.\n")


def show_menu():
    print("===== SMART PROJECT ARCHIVER =====")
    print("1. List Projects")
    print("2. Create Archive")
    print("3. View Archive Contents")
    print("4. Archive Statistics")
    print("5. Extract Archive")
    print("6. Delete Archive")
    print("7. Exit")


def main():
    create_required_folders()
    create_sample_projects()

    while True:

        show_menu()

        choice = input("\nEnter your choice: ").strip()

        print()

        if choice == "1":
            list_projects()

        elif choice == "2":
            create_archive()

        elif choice == "3":
            list_archive_contents()

        elif choice == "4":
            show_archive_statistics()

        elif choice == "5":
            extract_archive()

        elif choice == "6":
            delete_archive()

        elif choice == "7":
            print("Thank you for using Smart Project Archiver.")
            break

        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
    