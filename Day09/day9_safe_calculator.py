#Day9 Project
#Safe Calculator System

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

while True:
    print("\n====SAFE CALCULATOR====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "5":
        print("Calculator Closed.")
        break
    try:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number"))

        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            print("Result:", divide(num1, num2))

        else:
            print("Invalid Choice")
    except ValueError:
        print("Please enter valid numbers.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
