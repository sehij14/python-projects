# Day 14 Project
# Employee Management System

class Employee:

    def __init__(self, name, employee_id, salary):

        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_employee(self):

        print("\n----- EMPLOYEE INFO -----")
        print("Name :", self.name)
        print("ID :", self.employee_id)
        print("Salary :", self.salary)


class Developer(Employee):

    def __init__(self, name, employee_id, salary, language):

        super().__init__(name, employee_id, salary)

        self.language = language

    def display_developer(self):

        self.display_employee()

        print("Language :", self.language)

developer1 = Developer(
    "Rahul",
    101,
    50000,
    "Python"
)
developer2 = Developer(
    "Aman",
    102,
    65000,
    "Java"
)

developer1.display_developer()
developer2.display_developer()