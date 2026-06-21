from datetime import datetime

def write_log(message):

    file = open(
        "Day29/activity_log.txt",
        "a"
    )

    file.write(
        f"{datetime.now()} - {message}\n"
    )

    file.close()

while True:

    print("\n===== ACTIVITY LOGGER =====")

    print("1. Add Student")
    print("2. Delete Student")
    print("3. Create Backup")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        student_name = input(
            "Enter Student Name: "
        )

        print(
            f"{student_name} Added Successfully"
        )

        write_log(
            f"Student {student_name} Added"
        )

    elif choice == "2":

        student_name = input(
            "Enter Student Name: "
        )

        print(
            f"{student_name} Deleted Successfully"
        )

        write_log(
            f"Student {student_name} Deleted"
        )

    elif choice == "3":

        print(
            "Backup Created Successfully"
        )

        write_log(
            "Backup Created"
        )

    elif choice == "4":

        write_log(
            "Program Closed"
        )

        print(
            "Program Closed"
        )

        break

    else:

        print(
            "Invalid Choice"
        )

        write_log(
            "Invalid Menu Choice Entered"
        )