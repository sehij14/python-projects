# Day 11 Final Project
# Student Class System

class Student:

    def __init__(self, name, age, marks, city):

        self.name = name
        self.age = age
        self.marks = marks
        self.city = city

    def display_info(self):

        print("\n----- STUDENT INFO -----")
        print("Name :", self.name)
        print("Age :", self.age)
        print("Marks :", self.marks)
        print("City :", self.city)


student1 = Student("Sehijpreet", 18, 92, "Mohali")

student1.display_info()
