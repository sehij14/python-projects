from pathlib import Path


BASE_FOLDER = Path("Day48")
DATA_FOLDER = BASE_FOLDER / "data"
HISTORY_FILE = DATA_FOLDER / "processed_tasks.txt"

task_queue: list[str] = []


def create_required_folders() -> None:

    DATA_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )


def save_processed_task(task: str) -> None:

    with HISTORY_FILE.open(
        "a",
        encoding="utf-8"
    ) as file:

        file.write(task + "\n")


def add_task(task: str) -> None:

    task = task.strip()

    if not task:

        print("Task cannot be empty.\n")
        return

    task_queue.append(task)

    print(f"Task '{task}' added successfully.\n")