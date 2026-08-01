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
