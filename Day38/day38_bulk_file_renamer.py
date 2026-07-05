# Day38- Bulk File Renamer

import os

folder_path = "Day38/test_files"

while True:

    print("\nBULK FILE RENAMER UTILITY")
    print("1. View Files")
    print("2. Rename Files")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        try:

            files = os.listdir(folder_path)

            if len(files) == 0:
                print("\nNo files found.")

            else:

                print("\nFILES IN FOLDER\n")

                for file in files:
                    print(file)

        except FileNotFoundError:
            print("\nFolder does not exist.")

    elif choice == "2":

        try:

            files = os.listdir(folder_path)

            if len(files) == 0:
                print("\nNo files available for renaming.")

            else:

                prefix = input(
                    "\nEnter filename prefix: "
                )

                count = 1

                for file in files:

                    old_path = os.path.join(
                        folder_path,
                        file
                    )

                    filename, extension = os.path.splitext(
                        file
                    )

                    cleaned_name = (
                        prefix.lower()
                        .replace(" ", "_")
                    )

                    new_name = (
                        f"{cleaned_name}_{count}"
                        f"{extension.lower()}"
                    )

                    new_path = os.path.join(
                        folder_path,
                        new_name
                    )

                    os.rename(old_path, new_path)

                    print(
                        f"Renamed: "
                        f"{file} -> {new_name}"
                    )

                    count += 1

                print("\nBulk renaming completed.")

        except FileNotFoundError:
            print("\nFolder does not exist.")

    elif choice == "3":

        print("\nClosing Bulk File Renamer Utility.")
        break

    else:
        print("\nInvalid choice.") 