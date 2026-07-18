from pathlib import Path


BASE_FOLDER = Path("Day45")
LOG_FOLDER = BASE_FOLDER / "logs"
FILTER_FOLDER = BASE_FOLDER / "filtered_logs"

LOG_FILE = LOG_FOLDER / "application.log"


SAMPLE_LOGS = [
    "INFO User logged in",
    "INFO Configuration loaded",
    "WARNING Low disk space",
    "ERROR Database connection failed",
    "INFO File uploaded",
    "WARNING Password expires soon",
    "ERROR Backup failed",
    "INFO User logged out"
]


def create_required_folders():

    LOG_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    FILTER_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )


def create_log_file():

    if LOG_FILE.exists():
        return

    LOG_FILE.write_text(
        "\n".join(SAMPLE_LOGS),
        encoding="utf-8"
    )


def log_generator():

    with LOG_FILE.open(
        "r",
        encoding="utf-8"
    ) as file:

        for line in file:

            yield line.strip()


def display_logs():

    print("\nApplication Logs\n")

    found = False

    for log in log_generator():

        found = True
        print(log)

    if not found:
        print("No logs available.")

    print()