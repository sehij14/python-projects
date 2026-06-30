# Day32 / Workforce Management System

class Employee:

    company_name = "TechVision Solutions"

    def __init__(self, employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary

    def display_employee(self):
        print("\n----- EMPLOYEE DETAILS -----")
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)
        print("Company Name:", Employee.company_name)

    @classmethod
    def change_company_name(cls, new_company_name):
        cls.company_name = new_company_name


employees = []

while True:

    print("\n========== WORKFORCE MANAGEMENT SYSTEM ==========")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Change Company Name")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        try:
            employee_id = int(input("Enter Employee ID: "))
            name = input("Enter Employee Name: ")
            department = input("Enter Department: ")
            salary = float(input("Enter Salary: "))

            employee = Employee(employee_id, name, department, salary)

            employees.append(employee)

            print("\nEmployee added successfully.")

        except ValueError:
            print("\nInvalid input. Please enter correct data types.")

    elif choice == "2":

        if len(employees) == 0:
            print("\nNo employees available.")

        else:
            print("\n========== WORKFORCE RECORDS ==========")

            for employee in employees:
                employee.display_employee()

    elif choice == "3":

        new_company_name = input("Enter New Company Name: ")

        Employee.change_company_name(new_company_name)

        print("\nCompany name updated successfully.")

    elif choice == "4":

        print("\nExiting Employee Management System.")
        break

    else:
        print("\nInvalid choice. Please select a valid option.")