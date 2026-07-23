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