from enum import Enum
from pathlib import Path
from datetime import datetime
import json


BASE_FOLDER = Path("Day50")
DATA_FOLDER = BASE_FOLDER / "data"
PROJECT_FILE = DATA_FOLDER / "projects.json"


class ProjectStatus(Enum):

    PLANNED = "Planned"
    IN_PROGRESS = "In Progress"
    TESTING = "Testing"
    COMPLETED = "Completed"


class ProjectPriority(Enum):

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


def create_required_folders() -> None:

    DATA_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )


def load_projects() -> list:

    if not PROJECT_FILE.exists():
        return []

    with PROJECT_FILE.open(
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_projects(
    projects: list
) -> None:

    with PROJECT_FILE.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            projects,
            file,
            indent=4
        )


def get_current_time() -> str:

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M")


def create_project() -> None:

    projects = load_projects()

    name = input(
        "Project Name: "
    ).strip()

    if not name:

        print("Project name cannot be empty.\n")
        return

    description = input(
        "Description: "
    ).strip()

    tags = input(
        "Tags (comma separated): "
    ).split(",")

    tags = [
        tag.strip()
        for tag in tags
        if tag.strip()
    ]

    print("\nPriority")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    priority_choice = input(
        "Choose Priority: "
    ).strip()

    priority_map = {
        "1": ProjectPriority.LOW,
        "2": ProjectPriority.MEDIUM,
        "3": ProjectPriority.HIGH
    }

    if priority_choice not in priority_map:

        print("Invalid priority.\n")
        return

    current_time = get_current_time()

    projects.append(
        {
            "name": name,
            "description": description,
            "status": ProjectStatus.PLANNED.value,
            "priority": priority_map[
                priority_choice
            ].value,
            "tags": tags,
            "created": current_time,
            "updated": current_time
        }
    )

    save_projects(projects)

    print("\nProject created successfully.\n")

def view_projects() -> None:

    projects = load_projects()

    if not projects:
        print("\nNo projects found.\n")
        return

    print("\n===== PROJECTS =====\n")

    for index, project in enumerate(projects, start=1):

        print(f"{index}. {project['name']}")
        print(f"   Description : {project['description']}")
        print(f"   Status      : {project['status']}")
        print(f"   Priority    : {project['priority']}")
        print(f"   Tags        : {', '.join(project['tags'])}")
        print(f"   Created     : {project['created']}")
        print(f"   Updated     : {project['updated']}")
        print()

def search_projects() -> None:

    projects = load_projects()

    if not projects:
        print("\nNo projects available.\n")
        return

    keyword = input(
        "\nEnter project name or tag: "
    ).strip().lower()

    found = False

    for project in projects:

        if (
            keyword in project["name"].lower()
            or any(
                keyword in tag.lower()
                for tag in project["tags"]
            )
        ):

            print()
            print(project["name"])
            print(f"Status   : {project['status']}")
            print(f"Priority : {project['priority']}")
            print(f"Tags     : {', '.join(project['tags'])}")
            print()

            found = True

    if not found:
        print("\nNo matching project found.\n")

def update_project() -> None:

    projects = load_projects()

    if not projects:
        print("\nNo projects available.\n")
        return

    view_projects()

    try:

        choice = int(
            input(
                "\nSelect project number: "
            )
        )

    except ValueError:

        print("Invalid input.\n")
        return

    if choice < 1 or choice > len(projects):

        print("Invalid project number.\n")
        return

    print("\nSelect Status")
    print("1. Planned")
    print("2. In Progress")
    print("3. Testing")
    print("4. Completed")

    status_choice = input(
        "Choice: "
    ).strip()

    status_map = {
        "1": ProjectStatus.PLANNED,
        "2": ProjectStatus.IN_PROGRESS,
        "3": ProjectStatus.TESTING,
        "4": ProjectStatus.COMPLETED
    }

    if status_choice not in status_map:

        print("Invalid status.\n")
        return

    projects[
        choice - 1
    ]["status"] = status_map[
        status_choice
    ].value

    projects[
        choice - 1
    ]["updated"] = get_current_time()

    save_projects(projects)

    print("\nProject updated successfully.\n")

def delete_project() -> None:

    projects = load_projects()

    if not projects:
        print("\nNo projects available.\n")
        return

    view_projects()

    try:

        choice = int(
            input(
                "\nSelect project number to delete: "
            )
        )

    except ValueError:

        print("Invalid input.\n")
        return

    if choice < 1 or choice > len(projects):

        print("Invalid project number.\n")
        return

    removed = projects.pop(
        choice - 1
    )

    save_projects(projects)

    print(
        f"\nDeleted: {removed['name']}\n"
    )


def project_statistics() -> None:

    projects = load_projects()

    total = len(projects)

    planned = sum(
        project["status"] == ProjectStatus.PLANNED.value
        for project in projects)

    progress = sum(
        project["status"] == ProjectStatus.IN_PROGRESS.value
        for project in projects)

    testing = sum(
        project["status"] == ProjectStatus.TESTING.value
        for project in projects)

    completed = sum(
        project["status"] == ProjectStatus.COMPLETED.value
        for project in projects)

    print("\n===== STATISTICS =====\n")

    print(f"Total Projects : {total}")
    print(f"Planned        : {planned}")
    print(f"In Progress    : {progress}")
    print(f"Testing        : {testing}")
    print(f"Completed      : {completed}")
    print()


def show_menu() -> None:

    print("\n===== DEVELOPER WORKSPACE MANAGER =====")
    print("1. Create Project")
    print("2. View Projects")
    print("3. Search Project")
    print("4. Update Project")
    print("5. Delete Project")
    print("6. Project Statistics")
    print("7. Exit")


def main() -> None:

    create_required_folders()

    while True:

        show_menu()

        choice = input(
            "\nChoose an option: "
        ).strip()

        if choice == "1":

            create_project()

        elif choice == "2":

            view_projects()

        elif choice == "3":

            search_projects()

        elif choice == "4":

            update_project()

        elif choice == "5":

            delete_project()

        elif choice == "6":

            project_statistics()

        elif choice == "7":

            print("\nThank you for using Developer Workspace Manager.")

            break

        else:

            print("\nInvalid choice.\n")


if __name__ == "__main__":

    main()