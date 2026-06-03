# Day3 Final Project
#Smart User Decision System
print("---WELCOME TO SMART SYSTEM---")

#Taking user input
name = input("Enter your name:")
age = int(input("Enter your age:"))
marks = int(input("Enter your marks:"))
number = int(input("Enter a number:"))
print("\n---RESULTS---")

#Voting eligibility
if age >= 18:
    print(name, "you are eligible to vote")
else:
    print(name, "you are not eligible to vote")

#Grade system
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade:B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Result: Fail")

#Even or Odd
if number % 2 ==0:
    print("The number is Even")
else:
    print("The number is Odd")

#Positive or Negative
if number > 0:
    print("The number is Positive")
elif number < 0:
    print("The number is Negative")
else:
    print("The number is Zero")

print("\n---THANK YOU---")
