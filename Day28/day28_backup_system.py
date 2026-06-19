import sqlite3

connection = sqlite3.connect(
    "Day28/school_day28.db"
)
print("Database Created")
connection.close()

import shutil

while True:

    print("\n===== DATABASE BACKUP SYSTEM =====")

    print("1. Create Backup")
    print("2. Restore Backup")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        try:

            backup_number = int(
                input("Enter Backup Number: ")
            )

            backup_name = (
                f"Day28/school_backup_{backup_number}.db"
            )

            shutil.copy(
                "Day28/school_day28.db",
                backup_name
            )

            print(
                f"Backup Created Successfully: {backup_name}"
            )

        except FileNotFoundError:

            print(
                "Database File Not Found"
            )

        except ValueError:

            print(
                "Please Enter Valid Number"
            )

    elif choice == "2":

        try:

            backup_number = int(
                input(
                    "Enter Backup Number To Restore: "
                )
            )

            backup_name = (
                f"Day28/school_backup_{backup_number}.db"
            )

            shutil.copy(
                backup_name,
                "Day28/school_day28.db"
            )

            print(
                "Database Restored Successfully!"
            )

        except FileNotFoundError:

            print(
                "Backup File Not Found"
            )

        except ValueError:

            print(
                "Please Enter Valid Number"
            )

    elif choice == "3":

        print(
            "Program Closed"
        )

        break

    else:

        print(
            "Invalid Choice"
        )