# Day 17 Project
# Student Record System with Special Methods

class Student:

    def __init__(self, name, marks):

        self.name = name
        self.marks = marks

    def __str__(self):

        return f"Student: {self.name} | Marks: {self.marks}"

    def __len__(self):

        return len(self.name)

    def __add__(self, other):

        return self.marks + other.marks
    
    def __sub__(self, other):

        return self.marks - other.marks

student1 = Student("Rahul", 90)

student2 = Student("Aman", 85)

student3 = Student("Priya", 95)

print(student1)
print(student2)
print(student3)

print("\nLength of Student1 Name:")
print(len(student1))

print("\nCombined Marks:")
print(student1 + student2)

print("\nCombined Marks:")
print(student2 + student3)

print("\nDifference in Marks:")
print(student3 - student1)