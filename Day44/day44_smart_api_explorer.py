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

def save_response(posts):

    if not posts:
        print("No data available to save.\n")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    file_path = (
        RESPONSE_FOLDER /
        f"response_{timestamp}.json"
    )

    file_path.write_text(
        json.dumps(posts, indent=4),
        encoding="utf-8"
    )

    log_request(
        f"Response saved to {file_path.name}"
    )

    print("Response saved successfully.\n")


def search_post(posts):

    if not posts:
        print("No data available.\n")
        return

    try:
        post_id = int(input("Enter Post ID: "))
    except ValueError:
        print("Please enter a valid number.\n")
        return

    for post in posts:

        if post["id"] == post_id:

            print("\nPost Found\n")
            print(f"ID      : {post['id']}")
            print(f"User ID : {post['userId']}")
            print(f"Title   : {post['title']}")
            print(f"Body    : {post['body']}\n")

            return

    print("Post not found.\n")


def show_statistics(posts):

    if not posts:
        print("No data available.\n")
        return

    users = {
        post["userId"]
        for post in posts
    }

    print("\nAPI Statistics")
    print("----------------------------")
    print(f"Total Posts : {len(posts)}")
    print(f"Unique Users: {len(users)}")
    print()


def view_request_history():

    print("\nRequest History\n")

    history = LOG_FILE.read_text(
        encoding="utf-8"
    )

    if not history.strip():
        print("No requests logged yet.\n")
        return

    print(history)