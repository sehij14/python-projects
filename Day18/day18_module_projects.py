# Main Program

import student_utils


student1_marks = 92

student2_marks = 78

student3_marks = 35

print("Student 1 Grade:",
      student_utils.calculate_grade(student1_marks))

print("Student 2 Grade:",
      student_utils.calculate_grade(student2_marks))

print("Student 3 Grade:",
      student_utils.calculate_grade(student3_marks))


print()

print("Student 1 Result:",
      student_utils.check_result(student1_marks))

print("Student 2 Result:",
      student_utils.check_result(student2_marks))

print("Student 3 Result:",
      student_utils.check_result(student3_marks))