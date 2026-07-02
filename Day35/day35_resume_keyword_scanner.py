# Day35- Resume Keyword Scanner

required_skills = [
    "python",
    "sql",
    "git",
    "communication",
    "problem solving",
    "oop",
    "teamwork",
    "debugging"
]

resume_text = ""

while True:

    print("\nRESUME KEYWORD SCANNER")
    print("1. Enter Resume Text")
    print("2. Analyze Resume")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        print("\nPaste your resume text below:")
        resume_text = input().lower()

        print("\nResume text saved successfully.")

    elif choice == "2":

        if len(resume_text) == 0:
            print("\nNo resume text available.")
            continue

        matched_skills = []
        missing_skills = []

        for skill in required_skills:

            if skill in resume_text:
                matched_skills.append(skill)

            else:
                missing_skills.append(skill)

        score = (
            len(matched_skills) / len(required_skills)
        ) * 100

        print("\nRESUME ANALYSIS REPORT")

        print("\nMatched Skills:")
        for skill in matched_skills:
            print("-", skill)

        print("\nMissing Skills:")
        for skill in missing_skills:
            print("-", skill)

        print(f"\nResume Match Score: {score:.2f}%")

        if score >= 80:
            print("Strong resume match.")

        elif score >= 50:
            print("Moderate resume match.")

        else:
            print("Resume needs improvement.")

    elif choice == "3":

        print("\nClosing Resume Keyword Scanner.")
        break

    else:
        print("\nInvalid choice.")