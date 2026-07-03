# Day36/ Smart Expense Analytics Tracker

expenses = []

while True:

    print("\nSMART EXPENSE ANALYTICS TRACKER")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Generate Analytics Report")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        title = input("Enter expense title: ")
        category = input("Enter category: ")
        period = input("Enter period (weekly/monthly): ").lower()

        try:
            amount = float(input("Enter amount: "))

            expense = {
                "title": title,
                "category": category,
                "amount": amount,
                "period": period
            }

            expenses.append(expense)

            print("\nExpense added successfully.")

        except ValueError:
            print("\nInvalid amount entered.")

    elif choice == "2":

        if len(expenses) == 0:
            print("\nNo expenses available.")

        else:

            print("\nALL EXPENSES")

            for expense in expenses:

                print(
                    f"{expense['title']} | "
                    f"{expense['category']} | "
                    f"{expense['period']} | "
                    f"₹{expense['amount']}"
                )

    elif choice == "3":

        if len(expenses) == 0:
            print("\nNo expense data available.")
            continue

        total_spending = 0
        weekly_total = 0
        monthly_total = 0

        category_totals = {}

        highest_expense = expenses[0]

        for expense in expenses:

            amount = expense["amount"]
            category = expense["category"]
            period = expense["period"]

            total_spending += amount

            if period == "weekly":
                weekly_total += amount

            elif period == "monthly":
                monthly_total += amount

            if category not in category_totals:
                category_totals[category] = 0

            category_totals[category] += amount

            if amount > highest_expense["amount"]:
                highest_expense = expense

        highest_category = max(
            category_totals,
            key=category_totals.get
        )

        print("\nEXPENSE ANALYTICS REPORT")

        print(f"\nTotal Spending: ₹{total_spending}")

        print(f"Weekly Spending: ₹{weekly_total}")

        print(f"Monthly Spending: ₹{monthly_total}")

        print("\nCATEGORY-WISE BREAKDOWN")

        for category, amount in category_totals.items():
            print(f"{category}: ₹{amount}")

        print("\nHIGHEST SPENDING CATEGORY")

        print(
            f"{highest_category} "
            f"(₹{category_totals[highest_category]})"
        )

        print("\nHIGHEST INDIVIDUAL EXPENSE")

        print(
            f"{highest_expense['title']} "
            f"- ₹{highest_expense['amount']}"
        )

        print("\nSPENDING INSIGHT")

        if total_spending > 10000:
            print("Your spending is relatively high.")

        elif total_spending > 5000:
            print("Your spending is moderate.")

        else:
            print("Your spending is currently controlled.")

    elif choice == "4":

        print("\nClosing Smart Expense Analytics Tracker.")
        break

    else:
        print("\nInvalid choice.")