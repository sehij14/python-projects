# Day5 Project
#Student Report System using Functions

print("------STUDENT REPORT SYSTEM------")

#Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >=75:
        return "B"
    elif marks >=50:
        return "C"
    else:
        return "Fail"
    
#Function to check pass/fail
def check_result(marks):
        if marks >=40:
            return "Pass"
        else:
            return "Fail"

#Function to display report
def display_report(name, marks):
    grade = calculate_grade(marks)
    result = check_result(marks)

    print("\n-----REPORT-----")
    print("Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)  
    print("Result:", result)

#Main program
name = input("Enter student name:")
marks = int(input("Enter marks:"))

display_report(name, marks)
print("\n-----THANK YOU-----")
