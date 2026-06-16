# Day13 Project
# Student Security System

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks
    
    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks
        else:
            print("Invalid Marks!")

    def display_info(self):
            print("\n-----STUDENT INFO-----")
            print("Name :", self.name)
            print("Marks :", self.__marks)

student1 = Student("Rahul", 90)
student2 = Student("Aman", 85)
student1.display_info()
student2.display_info()

print("\nCurrent Marks of Student 1:")
print(student1.get_marks())

student1.set_marks(95)
print("\nAfter Updating Marks:")
student1.display_info()
student1.set_marks(-50)
