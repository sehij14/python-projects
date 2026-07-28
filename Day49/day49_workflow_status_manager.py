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

def read_workflows() -> list[str]:

    if not WORKFLOW_FILE.exists():
        return []

    return WORKFLOW_FILE.read_text(
        encoding="utf-8"
    ).splitlines()

def view_workflows() -> None:

    workflows = read_workflows()

    if not workflows:

        print("No workflows found.\n")
        return

    print("\nSaved Workflows")
    print("----------------")

    for index, workflow in enumerate(
        workflows,
        start=1
    ):
        print(f"{index}. {workflow}")

    print()


def update_workflow_status() -> None:

    workflows = read_workflows()

    if not workflows:

        print("No workflows available.\n")
        return

    view_workflows()

    try:

        choice = int(
            input(
                "Select workflow number: "
            )
        )

        if choice < 1 or choice > len(workflows):

            print("Invalid workflow number.\n")
            return

    except ValueError:

        print("Please enter a valid number.\n")
        return

    print("\nChoose New Status")
    print("1. Pending")
    print("2. In Progress")
    print("3. Completed")
    print("4. Cancelled")

    status_choice = input(
        "Enter your choice: "
    ).strip()

    status_map = {
        "1": WorkflowStatus.PENDING,
        "2": WorkflowStatus.IN_PROGRESS,
        "3": WorkflowStatus.COMPLETED,
        "4": WorkflowStatus.CANCELLED
    }

    if status_choice not in status_map:

        print("Invalid status.\n")
        return

    task_name = workflows[
        choice - 1
    ].split(" | ")[0]

    workflows[
        choice - 1
    ] = (
        f"{task_name} | "
        f"{status_map[status_choice].value}"
    )

    WORKFLOW_FILE.write_text(
        "\n".join(workflows) + "\n",
        encoding="utf-8"
    )

    print("Workflow updated successfully.\n")

def show_menu() -> None:

    print("===== WORKFLOW STATUS MANAGER =====")
    print("1. Create Workflow")
    print("2. View Workflows")
    print("3. Update Workflow Status")
    print("4. Exit")


def main() -> None:

    create_required_folders()

    while True:

        show_menu()

        choice = input(
            "\nEnter your choice: "
        ).strip()

        print()

        if choice == "1":

            create_workflow()

        elif choice == "2":

            view_workflows()

        elif choice == "3":

            update_workflow_status()

        elif choice == "4":

            print("Thank you for using "
                "Workflow Status Manager.")
            break

        else:

            print("Invalid choice.\n")

if __name__ == "__main__":

    main()