# Day 8 Project
# Contact Book using File Handling

FILE_NAME = "contacts.txt"

def add_contact():

    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")

    file = open(FILE_NAME, "a")

    file.write(name + " - " + phone + "\n")

    file.close()

    print("Contact Saved Successfully!")

def view_contacts():

    try:

        file = open(FILE_NAME, "r")

        content = file.read()

        file.close()

        if content == "":
            print("No Contacts Found.")

        else:
            print("\n------ CONTACT LIST ------")
            print(content)

    except FileNotFoundError:

        print("No Contacts Saved Yet.")

while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        print("Program Closed.")
        break

    else:
        print("Invalid Choice")