# Student Utility Module

def calculate_grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 75:
        return "B"

    elif marks >= 50:
        return "C"

    else:
        return "Fail"

def check_result(marks):

    if marks >= 40:
        return "Pass"

    return "Fail"