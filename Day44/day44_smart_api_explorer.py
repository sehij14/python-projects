from pathlib import Path
from datetime import datetime
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import json


BASE_FOLDER = Path("Day44")
LOG_FOLDER = BASE_FOLDER / "api_logs"
RESPONSE_FOLDER = BASE_FOLDER / "saved_responses"
LOG_FILE = LOG_FOLDER / "request_history.txt"


API_URL = "https://jsonplaceholder.typicode.com/posts"


def create_required_folders():
    LOG_FOLDER.mkdir(parents=True, exist_ok=True)
    RESPONSE_FOLDER.mkdir(parents=True, exist_ok=True)

    if not LOG_FILE.exists():
        LOG_FILE.write_text("", encoding="utf-8")


def log_request(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with LOG_FILE.open(
        "a",
        encoding="utf-8"
    ) as file:

        file.write(f"[{timestamp}] {message}\n")


def fetch_data():

    try:

        with urlopen(API_URL) as response:

            status_code = response.status

            data = json.loads(
                response.read().decode("utf-8")
            )

            log_request(
                f"GET request successful ({status_code})"
            )

            return status_code, data

    except HTTPError as error:

        log_request(
            f"HTTP Error: {error.code}"
        )

        print(f"HTTP Error: {error.code}\n")

    except URLError:

        log_request(
            "Network connection failed."
        )

        print("Unable to connect to the internet.\n")

    return None, None


def display_posts(posts):

    if not posts:
        print("No data available.\n")
        return

    print("\nLatest Posts\n")

    for post in posts[:5]:

        print("-" * 40)
        print(f"ID      : {post['id']}")
        print(f"Title   : {post['title']}")
        print(f"User ID : {post['userId']}")
        print()