# Day15 Project
# Company Management System

class Employee:

    def __init__(self, name):

        self.name = name

    def work(self):

        print(self.name, "is working")


class Developer(Employee):

    def work(self):

        print(self.name, "is writing Python code")


class Manager(Employee):

    def work(self):

        print(self.name, "is managing the team")


class Designer(Employee):

    def work(self):

        print(self.name, "is creating UI designs")


employee1 = Employee("Rahul")

developer1 = Developer("Aman")

developer2 = Developer("Riya")

manager1 = Manager("Karan")

designer1 = Designer("Priya")

employee1.work()

developer1.work()

developer2.work()

manager1.work()

designer1.work()