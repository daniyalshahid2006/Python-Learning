import csv

headers = ["employee_id", "employee_name", "gmail", "department", "position", "salary"]
class Employee:
    def __init__(self, employee_id, employee_name, gmail, department, position, salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.gmail = gmail
        self.department = department
        self.position = position
        self.salary = salary


class EmployeeManager:
    def __init__(self):
        self.employees = {}

    def add_existing_employee(self, employee_id, employee_name, gmail, department, position, salary):
        if employee_id in self.employees:
            print("Employee already exists chnage id")
        else:
            employee = Employee(employee_id, employee_name, gmail, department, position, salary)
            self.employees[employee_id] = employee

    def add_emp(self, employee_name, gmail, department, position, salary):
        candidate = 1
        while candidate in self.employees:
            candidate = candidate + 1
        employee = Employee(candidate, employee_name, gmail, department, position, salary)
        self.employees[candidate] = employee

    def show_employees(self):
        for employee in self.employees.values():
            print(employee.employee_id)
            print(employee.employee_name)
            print(employee.gmail)
            print(employee.department)
            print(employee.position)
            print(employee.salary)

    def search_employee(self):
        search_id = int(input("Enter employee id: "))
        if search_id in self.employees:
            print(self.employees[search_id].employee_name)
            print(self.employees[search_id].gmail)
            print(self.employees[search_id].department)
            print(self.employees[search_id].position)
            print(self.employees[search_id].salary)
        else:
            print("Employee not found")

    def remove_employee(self):
        search_id = int(input("Enter employee id you want to remove: "))
        if search_id in self.employees:
            del self.employees[search_id]
            print("Employee removed")
        else:
            print("Employee not found")
    def save_employee(self):
        with open('employees.csv', "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            for employee in self.employees.values():
                writer.writerow([employee.employee_id, employee.employee_name, employee.gmail,employee.department, employee.position, employee.salary])
    def update_employee(self):
        id = int(input("Enter employee id: "))
        if id not in self.employees:
            print("Employee not found")
        else:
            pick = 0
            while pick != 6:
                print("what you want to update?")
                print("1.name")
                print("2.email")
                print("3.department")
                print("4.position")
                print("5.salary")
                print("6.exit")
                pick = int(input("Enter your choice: "))
                if pick == 1:
                    new_name = input("Enter new employee name: ")
                    self.employees[id].employee_name = new_name
                elif pick == 2:
                    new_email = input("Enter new employee email: ")
                    self.employees[id].gmail = new_email
                elif pick == 3:
                    new_department = input("Enter new employee department: ")
                    self.employees[id].department= new_department
                elif pick == 4:
                    new_position = input("Enter new employee position: ")
                    self.employees[id].position = new_position
                elif pick == 5:
                    new_salary = input("Enter new employee salary: ")
                    self.employees[id].salary = new_salary
                elif pick == 6:
                    print("exit")

employee_manager = EmployeeManager()



with open('employees.csv', "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        employee_id = int(row[0])
        employee_name = row[1]
        gmail = row[2]
        department = row[3]
        position = row[4]
        salary = row[5]

        employee_manager.add_existing_employee(
            employee_id, employee_name, gmail, department, position, salary
        )

employee_manager.show_employees()
employee_manager.remove_employee()
employee_manager.save_employee()