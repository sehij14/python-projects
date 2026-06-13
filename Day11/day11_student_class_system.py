# Day 11 Project
# Student Class System

class Student:

    def __init__(self, name, age, marks):

        self.name = name
        self.age = age
        self.marks = marks

    def display_info(self):

        print("\n----- STUDENT INFO -----")
        print("Name :", self.name)
        print("Age :", self.age)
        print("Marks :", self.marks)


student1 = Student("Sehijpreet", 18, 92)

student1.display_info()
