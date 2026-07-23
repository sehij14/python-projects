from pathlib import Path
from time import perf_counter


BASE_FOLDER = Path("Day46")
LOG_FOLDER = BASE_FOLDER / "logs"
LOG_FILE = LOG_FOLDER / "function_log.txt"

CALL_COUNTS = {}


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


def performance_monitor(function):

    def wrapper():

        function_name = function.__name__

        CALL_COUNTS[function_name] = (
            CALL_COUNTS.get(function_name, 0) + 1
        )

        start_time = perf_counter()

        print(f"\nRunning {function_name}...")

        function()

        end_time = perf_counter()

        execution_time = (
            end_time - start_time
        )

        message = (
            f"{function_name} | "
            f"Run #{CALL_COUNTS[function_name]} | "
            f"{execution_time:.6f} seconds"
        )

        write_log(message)

        print(
            f"Finished in "
            f"{execution_time:.6f} seconds."
        )

    return wrapper

@performance_monitor
def generate_report():

    print("Generating monthly performance report...")


@performance_monitor
def clean_temp_files():

    print("Cleaning temporary files...")


@performance_monitor
def backup_project():

    print("Creating project backup...")


def show_call_statistics():

    if not CALL_COUNTS:

        print("\nNo functions have been executed yet.\n")
        return

    print("\nFunction Call Statistics")
    print("------------------------")

    for function_name, count in CALL_COUNTS.items():

        print(f"{function_name:<20} {count}")

    print()


def view_log_history():

    if not LOG_FILE.exists():

        print("\nNo log history found.\n")
        return

    print("\nExecution Log History")
    print("---------------------")

    with LOG_FILE.open(
        "r",
        encoding="utf-8"
    ) as file:

        content = file.read().strip()

    if content:

        print(content)

    else:

        print("Log file is empty.")

    print()

def show_menu():

    print("===== FUNCTION PERFORMANCE MONITOR =====")
    print("1. Generate Report")
    print("2. Clean Temporary Files")
    print("3. Backup Project")
    print("4. View Function Call Statistics")
    print("5. View Execution Log")
    print("6. Exit")


def main():

    create_required_folders()

    while True:

        show_menu()

        choice = input("\nEnter your choice: ").strip()

        print()

        if choice == "1":

            generate_report()

        elif choice == "2":

            clean_temp_files()

        elif choice == "3":

            backup_project()

        elif choice == "4":

            show_call_statistics()

        elif choice == "5":

            view_log_history()

        elif choice == "6":

            print("Thank you for using Function Performance Monitor.")
            break

        else:

            print("Invalid choice.\n")


if __name__ == "__main__":

    main()