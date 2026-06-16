import csv

total_marks = 0

student_count = 0

topper_name = ""

highest_marks = 0

file = open("Day19/students.csv", "r")

reader = csv.DictReader(file)

for row in reader:

    name = row["Name"]

    marks = int(row["Marks"])

    total_marks += marks

    student_count += 1

    if marks > highest_marks:

        highest_marks = marks

        topper_name = name

file.close()

average_marks = total_marks / student_count

print("----- STUDENT REPORT -----")

print("Total Students:", student_count)

print("Average Marks:", average_marks)

print("Topper:", topper_name)

print("Highest Marks:", highest_marks)