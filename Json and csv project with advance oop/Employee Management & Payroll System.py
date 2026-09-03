import csv


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


employee_manager = EmployeeManager()


with open('employees.csv', "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["employee_id", "employee_name", "gmail", "department", "position", "salary"])
    writer.writerows([
        [1, "dani", "gmail", "ai", "employee", "100k"],
        [2, "pani", "gmail", "ai", "employee", "100k"]
    ])


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