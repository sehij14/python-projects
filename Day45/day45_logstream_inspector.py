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

def filter_logs(level):

    filtered_logs = []

    for log in log_generator():

        if log.startswith(level.upper()):

            filtered_logs.append(log)

    return filtered_logs


def save_filtered_logs(level):

    logs = filter_logs(level)

    if not logs:
        print(f"No {level.upper()} logs found.\n")
        return

    output_file = (
        FILTER_FOLDER /
        f"{level.lower()}_logs.txt"
    )

    output_file.write_text(
        "\n".join(logs),
        encoding="utf-8"
    )

    print(
        f"{len(logs)} log(s) saved to "
        f"{output_file.name}\n"
    )


def show_statistics():

    counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    total = 0

    for log in log_generator():

        total += 1

        for level in counts:

            if log.startswith(level):

                counts[level] += 1

    print("\nLog Statistics")
    print("-------------------------")
    print(f"Total Logs : {total}")

    for level, count in counts.items():

        print(f"{level:<8}: {count}")

    print()


def search_logs():

    keyword = input(
        "Enter keyword to search: "
    ).strip().lower()

    print()

    found = False

    for log in log_generator():

        if keyword in log.lower():

            print(log)
            found = True

    if not found:

        print("No matching logs found.")

    print()