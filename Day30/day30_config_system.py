import json

try:

    file = open(
        "Day30/config.json",
        "r"
    )

    config = json.load(file)

    file.close()

    while True:

        print("\n===== SCHOOL CONFIGURATION SYSTEM =====")

        print("1. Show School Name")
        print("2. Show Passing Marks")
        print("3. Show Maximum Students")
        print("4. Show All Settings")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":

            print(
                f"School Name: {config['school_name']}"
            )

        elif choice == "2":

            print(
                f"Passing Marks: {config['passing_marks']}"
            )

        elif choice == "3":

            print(
                f"Maximum Students: {config['max_students']}"
            )

        elif choice == "4":

            for key, value in config.items():

                print(
                    f"{key} : {value}"
                )

        elif choice == "5":

            print(
                "Program Closed"
            )

            break

        else:

            print(
                "Invalid Choice"
            )

except FileNotFoundError:

    print(
        "Config File Not Found"
    )

except json.JSONDecodeError:

    print(
        "Invalid JSON Format"
    )