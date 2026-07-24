from pathlib import Path
from datetime import datetime


BASE_FOLDER = Path("Day47")
LOG_FOLDER = BASE_FOLDER / "logs"
LOG_FILE = LOG_FOLDER / "session_history.txt"


def create_required_folders():

    LOG_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )


def write_log(message):

    with LOG_FILE.open(
        "a",
        encoding="utf-8"
    ) as file:

        file.write(message + "\n")


class WorkspaceSession:

    def __init__(self, session_name):

        self.session_name = session_name

    def __enter__(self):

        start_time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        message = (
            f"START | "
            f"{self.session_name} | "
            f"{start_time}"
        )

        write_log(message)

        print(
            f"\nSession '{self.session_name}' started."
        )

        return self

    def __exit__(
        self,
        exception_type,
        exception_value,
        traceback
    ):

        end_time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        message = (
            f"END   | "
            f"{self.session_name} | "
            f"{end_time}"
        )

        write_log(message)

        print(
            f"Session '{self.session_name}' ended.\n"
        )

def perform_task():

    print("Working inside the session...")
    print("Saving project files...")
    print("Updating activity records...")
    print("Task completed successfully.\n")


def start_workspace_session():

    session_name = input(
        "Enter session name: "
    ).strip()

    if not session_name:

        print("Session name cannot be empty.\n")
        return

    with WorkspaceSession(session_name):

        perform_task()


def view_session_history():

    if not LOG_FILE.exists():

        print("\nNo session history found.\n")
        return

    print("\nWorkspace Session History")
    print("-------------------------")

    content = LOG_FILE.read_text(
        encoding="utf-8"
    ).strip()

    if content:

        print(content)

    else:

        print("History file is empty.")

    print()

def show_menu():

    print("===== WORKSPACE SESSION TRACKER =====")
    print("1. Start Workspace Session")
    print("2. View Session History")
    print("3. Exit")


def main():

    create_required_folders()

    while True:

        show_menu()

        choice = input(
            "\nEnter your choice: "
        ).strip()

        print()

        if choice == "1":

            start_workspace_session()

        elif choice == "2":

            view_session_history()

        elif choice == "3":

            print(
                "Thank you for using "
                "Workspace Session Tracker."
            )
            break

        else:

            print("Invalid choice.\n")


if __name__ == "__main__":

    main()