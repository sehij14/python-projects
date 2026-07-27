from enum import Enum
from pathlib import Path


BASE_FOLDER = Path("Day49")
DATA_FOLDER = BASE_FOLDER / "data"
WORKFLOW_FILE = DATA_FOLDER / "workflows.txt"


class WorkflowStatus(Enum):

    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


def create_required_folders() -> None:

    DATA_FOLDER.mkdir(
        parents=True,
        exist_ok=True)


def save_workflow(
    task_name: str,
    status: WorkflowStatus
) -> None:

    with WORKFLOW_FILE.open(
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            f"{task_name} | {status.value}\n")


def create_workflow() -> None:

    task_name = input(
        "Enter workflow name: ").strip()

    if not task_name:

        print("Workflow name cannot be empty.\n")
        return

    save_workflow(
        task_name,
        WorkflowStatus.PENDING)

    print("Workflow created successfully.\n")