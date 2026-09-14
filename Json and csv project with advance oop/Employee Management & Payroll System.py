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

    def search_employee(self,search_id):
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
                    new_salary = int(input("Enter new employee salary: "))
                    self.employees[id].salary = new_salary
                elif pick == 6:
                    print("exit")
class Payroll:
    def cal_salary(self):
        id = int(input("Enter employee id: "))
        if id in employee_manager.employees:
            months = int(input("Enter number of months: "))
            salary = employee_manager.employees[id].salary*months
            print(f"your salary of {months} months is {salary}")
    def ap_cal_salary(self):
        department = input("Enter department: ")
        total = 0
        found = False
        for employee in employee_manager.employees.values():
            if employee.department == department:
                total += employee.salary
                found = True
        if found:
         print(f"{department} department salary is {total}")
        else:
            print(f"department doesn't exist")


employee_manager = EmployeeManager()
payroll = Payroll()



with open('employees.csv', "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        employee_id = int(row[0])
        employee_name = row[1]
        gmail = row[2]
        department = row[3]
        position = row[4]
        salary = int(row[5])

        employee_manager.add_existing_employee(
            employee_id, employee_name, gmail, department, position, salary
        )

choice = ""
while choice != "9":
    print("======================")
    print("Employee Management System")
    print("======================")
    print("1. Add Employee")
    print("2. show Employee")
    print("3. search Employee")
    print("4. update Employee")
    print("5. remove Employee")
    print("6. Employee salary")
    print("7. department salary")
    print("8. save")
    print("9. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter employee name: ")
        gmail = input("Enter employee gmail: ")
        department = input("Enter employee department: ")
        position = input("Enter employee position: ")
        salary = int(input("Enter employee salary: "))
        employee_manager.add_emp(name,gmail,department,position,salary)
    elif choice == "2":
        employee_manager.show_employees()
    elif choice == "3":
        id = int(input("Enter employee id: "))
        employee_manager.search_employee(id)
    elif choice == "4":
        employee_manager.update_employee()
    elif choice == "5":
        employee_manager.remove_employee()
    elif choice == "6":
        payroll.cal_salary()
    elif choice == "7":
        payroll.ap_cal_salary()
    elif choice == "8":
        employee_manager.save_employee()
    elif choice == "9":
        print("Exit")
        break

