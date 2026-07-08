# Day40 code using python
# Password Strength Analyzer

import re

password_history = []

while True:

    print("\nPASSWORD STRENGTH ANALYZER")
    print("1. Analyze Password")
    print("2. View Password Analysis History")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        password = input(
            "\nEnter password to analyze: "
        )

        score = 0

        feedback = []

        if len(password) >= 8:
            score += 1
        else:
            feedback.append(
                "Password should be at least 8 characters."
            )

        if re.search(r"[A-Z]", password):
            score += 1
        else:
            feedback.append(
                "Add at least one uppercase letter."
            )

        if re.search(r"[a-z]", password):
            score += 1
        else:
            feedback.append(
                "Add at least one lowercase letter."
            )

        if re.search(r"\d", password):
            score += 1
        else:
            feedback.append(
                "Add at least one number."
            )

        if re.search(r"[!@#$%^&*]", password):
            score += 1
        else:
            feedback.append(
                "Add at least one special character."
            )

        if score == 5:
            strength = "Very Strong"

        elif score >= 4:
            strength = "Strong"

        elif score >= 3:
            strength = "Moderate"

        else:
            strength = "Weak"

        analysis = {
            "password": password,
            "score": score,
            "strength": strength
        }

        password_history.append(analysis)

        print("\nPASSWORD ANALYSIS REPORT")

        print(f"\nStrength: {strength}")
        print(f"Security Score: {score}/5")

        if len(feedback) > 0:

            print("\nSECURITY IMPROVEMENTS")

            for item in feedback:
                print("-", item)

        else:
            print(
                "\nExcellent password security."
            )

    elif choice == "2":

        if len(password_history) == 0:

            print("\nNo password analysis history.")

        else:

            print("\nPASSWORD ANALYSIS HISTORY\n")

            for item in password_history:

                print(
                    f"Password: {item['password']}"
                )

                print(
                    f"Strength: {item['strength']}"
                )

                print(
                    f"Score: {item['score']}/5\n"
                )

    elif choice == "3":

        print(
            "\nClosing Password Strength Analyzer."
        )

        break

    else:

        print("\nInvalid choice.")