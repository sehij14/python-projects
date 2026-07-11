from pathlib import Path

NOTES_FOLDER = Path("Day41") / "notes"
NOTES_FOLDER.mkdir(parents=True, exist_ok=True)


def sanitize_filename(title):
    """Convert note title into a safe filename."""

    filename = title.strip().lower()
    filename = filename.replace(" ", "_")

    safe_name = ""

    for character in filename:
        if character.isalnum() or character in ("_", "-"):
            safe_name += character

    return safe_name + ".md"


def create_note():
    print("\nCREATE NEW NOTE")

    title = input("Enter note title: ").strip()

    if title == "":
        print("Title cannot be empty.")
        return

    tags = input(
        "Enter tags (comma separated): "
    ).strip()

    print(
        "Enter note content "
        "(press Enter twice to finish):"
    )

    lines = []

    while True:
        line = input()

        if line == "":
            break

        lines.append(line)

    content = "\n".join(lines)

    filename = sanitize_filename(title)

    file_path = NOTES_FOLDER / filename

    if file_path.exists():
        print("A note with this title already exists.")
        return

    note_text = (
        f"# {title}\n\n"
        f"Tags: {tags}\n\n"
        f"{content}\n"
    )

    file_path.write_text(
        note_text,
        encoding="utf-8"
    )

    print("Note created successfully.")


def list_notes():

    print("\nALL NOTES\n")

    note_files = sorted(
        NOTES_FOLDER.glob("*.md")
    )

    if not note_files:
        print("No notes found.")
        return

    for index, file in enumerate(
        note_files,
        start=1
    ):
        print(f"{index}. {file.stem}")


def view_note():

    list_notes()

    filename = input(
        "\nEnter note filename: "
    ).strip()

    filename = sanitize_filename(filename)

    file_path = NOTES_FOLDER / filename

    if not file_path.exists():
        print("Note not found.")
        return

    print("\n----------------------\n")

    print(
        file_path.read_text(
            encoding="utf-8"
        )
    )

    print("\n----------------------")


def search_notes():

    keyword = input(
        "\nEnter keyword to search: "
    ).strip().lower()

    if keyword == "":
        print("Keyword cannot be empty.")
        return

    found = False

    print("\nSEARCH RESULTS\n")

    for file in NOTES_FOLDER.glob("*.md"):

        text = file.read_text(
            encoding="utf-8"
        ).lower()

        if keyword in text:

            found = True

            print(file.stem)

    if not found:
        print("No matching notes found.")


def search_by_tag():

    tag = input(
        "\nEnter tag to search: "
    ).strip().lower()

    if tag == "":
        print("Tag cannot be empty.")
        return

    found = False

    print("\nMATCHING NOTES\n")

    for file in sorted(
        NOTES_FOLDER.glob("*.md")
    ):

        text = file.read_text(
            encoding="utf-8"
        )

        lines = text.splitlines()

        if len(lines) >= 3:

            tag_line = lines[2]

            if tag_line.lower().startswith("tags:"):

                tags = (
                    tag_line[5:]
                    .strip()
                    .lower()
                    .split(",")
                )

                tags = [
                    item.strip()
                    for item in tags
                ]

                if tag in tags:

                    found = True

                    print(file.stem)

    if not found:
        print("No notes found with this tag.")


def delete_note():

    list_notes()

    filename = input(
        "\nEnter note filename to delete: "
    ).strip()

    filename = sanitize_filename(filename)

    file_path = NOTES_FOLDER / filename

    if not file_path.exists():
        print("Note not found.")
        return

    confirm = input(
        "Delete this note? (yes/no): "
    ).strip().lower()

    if confirm == "yes":

        file_path.unlink()

        print("Note deleted successfully.")

    else:

        print("Deletion cancelled.")


def show_statistics():

    note_files = list(
        NOTES_FOLDER.glob("*.md")
    )

    total_notes = len(note_files)

    total_tags = 0

    tag_counter = {}

    for file in note_files:

        text = file.read_text(
            encoding="utf-8"
        )

        lines = text.splitlines()

        if len(lines) >= 3:

            tag_line = lines[2]

            if tag_line.lower().startswith("tags:"):

                tags = [
                    tag.strip()
                    for tag in
                    tag_line[5:].split(",")
                    if tag.strip()
                ]

                total_tags += len(tags)

                for tag in tags:

                    tag = tag.lower()

                    if tag in tag_counter:
                        tag_counter[tag] += 1
                    else:
                        tag_counter[tag] = 1

    print("\nSMART NOTES STATISTICS\n")

    print(
        f"Total Notes : {total_notes}"
    )

    print(
        f"Total Tags  : {total_tags}"
    )

    if tag_counter:

        most_used = max(
            tag_counter,
            key=tag_counter.get
        )

        print(
            "Most Used Tag : "
            f"{most_used}"
        )

    else:

        print(
            "Most Used Tag : None"
        )


def display_menu():

    print("\nSMART NOTES CLI")
    print("-----------------------")
    print("1. Create Note")
    print("2. View All Notes")
    print("3. View Note")
    print("4. Search Notes")
    print("5. Search by Tag")
    print("6. Delete Note")
    print("7. Statistics")
    print("8. Exit")


def main():

    while True:

        display_menu()

        choice = input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":
            create_note()

        elif choice == "2":
            list_notes()

        elif choice == "3":
            view_note()

        elif choice == "4":
            search_notes()

        elif choice == "5":
            search_by_tag()

        elif choice == "6":
            delete_note()

        elif choice == "7":
            show_statistics()

        elif choice == "8":

            print(
                "\nThank you for using "
                "Smart Notes CLI."
            )

            break

        else:

            print(
                "Invalid choice. "
                "Please try again."
            )


if __name__ == "__main__":
    main() 
    
# hii
