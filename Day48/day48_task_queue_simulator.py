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


def process_next_task() -> None:

    if not task_queue:

        print("No pending tasks.\n")
        return

    task = task_queue.pop(0)

    save_processed_task(task)

    print(f"Processed task: {task}\n")


def view_pending_tasks() -> None:

    if not task_queue:

        print("No pending tasks.\n")
        return

    print("\nPending Tasks")
    print("-------------")

    for index, task in enumerate(task_queue, start=1):

        print(f"{index}. {task}")

    print()


def view_processed_history() -> None:

    if not HISTORY_FILE.exists():

        print("\nNo processed task history found.\n")
        return

    print("\nProcessed Task History")
    print("----------------------")

    content = HISTORY_FILE.read_text(
        encoding="utf-8"
    ).strip()

    if content:

        print(content)

    else:

        print("History file is empty.")

    print()

def show_menu() -> None:

    print("===== TASK QUEUE SIMULATOR =====")
    print("1. Add Task")
    print("2. Process Next Task")
    print("3. View Pending Tasks")
    print("4. View Processed Task History")
    print("5. Exit")


def main() -> None:

    create_required_folders()

    while True:

        show_menu()

        choice = input(
            "\nEnter your choice: "
        ).strip()

        print()

        if choice == "1":

            task = input(
                "Enter task name: "
            )

            add_task(task)

        elif choice == "2":

            process_next_task()

        elif choice == "3":

            view_pending_tasks()

        elif choice == "4":

            view_processed_history()

        elif choice == "5":

            print(
                "Thank you for using "
                "Task Queue Simulator."
            )
            break

        else:

            print("Invalid choice.\n")


if __name__ == "__main__":

    main()