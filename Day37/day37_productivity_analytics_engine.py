# Day37 
# Productivity Analytics Engine

from datetime import datetime

activities = []

while True:

    print("\nPRODUCTIVITY ANALYTICS ENGINE")
    print("1. Add Activity")
    print("2. View Activity Report")
    print("3. View Productivity Analytics")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        task = input("Enter activity name: ")
        category = input("Enter category: ")

        try:

            score = int(input("Enter productivity score (1-10): "))

            timestamp = datetime.now().strftime("%d-%m-%Y %H:%M")

            activity = {
                "task": task,
                "category": category,
                "score": score,
                "timestamp": timestamp
            }

            activities.append(activity)

            print("\nActivity logged successfully.")

        except ValueError:
            print("\nInvalid productivity score.")

    elif choice == "2":

        if len(activities) == 0:
            print("\nNo activities logged.")

        else:

            print("\nACTIVITY REPORT")

            for activity in activities:

                print(
                    f"{activity['task']} | "
                    f"{activity['category']} | "
                    f"Score: {activity['score']} | "
                    f"{activity['timestamp']}"
                )

    elif choice == "3":

        if len(activities) == 0:
            print("\nNo analytics available.")

        else:

            total_score = 0
            category_scores = {}

            highest_activity = activities[0]

            for activity in activities:

                total_score += activity["score"]

                category = activity["category"]

                if category not in category_scores:
                    category_scores[category] = 0

                category_scores[category] += activity["score"]

                if (
                    activity["score"]
                    > highest_activity["score"]
                ):
                    highest_activity = activity

            average_score = (
                total_score / len(activities)
            )

            print("\nPRODUCTIVITY ANALYTICS")

            print(
                f"\nTotal Productivity Score: "
                f"{total_score}"
            )

            print(
                f"Average Productivity Score: "
                f"{average_score:.2f}"
            )

            print("\nCATEGORY PERFORMANCE")

            for category, score in category_scores.items():

                print(f"{category}: {score}")

            print("\nMOST PRODUCTIVE ACTIVITY")

            print(
                f"{highest_activity['task']} "
                f"({highest_activity['score']})"
            )

    elif choice == "4":

        print("\nClosing Productivity Analytics Engine.")
        break

    else:
        print("\nInvalid choice.")