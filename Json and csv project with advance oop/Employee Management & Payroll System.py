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
            print("Employee already exists.")
        else:
            employee = Employee(
                employee_id,
                employee_name,
                gmail,
                department,
                position,
                salary
            )
            self.employees[employee_id] = employee

    def add_emp(self, employee_name, gmail, department, position, salary):
        candidate = 1

        while candidate in self.employees:
            candidate += 1

        employee = Employee(
            candidate,
            employee_name,
            gmail,
            department,
            position,
            salary
        )

        self.employees[candidate] = employee
        print(f"Employee added with ID {candidate}")

    def show_employees(self):
        if not self.employees:
            print("No employees found.")
            return

        for employee in self.employees.values():
            print("--------------------")
            print("ID:", employee.employee_id)
            print("Name:", employee.employee_name)
            print("Gmail:", employee.gmail)
            print("Department:", employee.department)
            print("Position:", employee.position)
            print("Salary:", employee.salary)

    def search_employee(self):
        try:
            search_id = int(input("Enter employee ID: "))
        except ValueError:
            print("Employee ID must be a number.")
            return

        if search_id in self.employees:
            employee = self.employees[search_id]

            print("--------------------")
            print("ID:", employee.employee_id)
            print("Name:", employee.employee_name)
            print("Gmail:", employee.gmail)
            print("Department:", employee.department)
            print("Position:", employee.position)
            print("Salary:", employee.salary)
        else:
            print("Employee not found.")

    def remove_employee(self):
        try:
            search_id = int(input("Enter employee ID you want to remove: "))
        except ValueError:
            print("Employee ID must be a number.")
            return

        if search_id in self.employees:
            del self.employees[search_id]
            print("Employee removed.")
        else:
            print("Employee not found.")

    def update_employee(self):
        try:
            employee_id = int(input("Enter employee ID: "))
        except ValueError:
            print("Employee ID must be a number.")
            return

        if employee_id not in self.employees:
            print("Employee not found.")
            return

        while True:
            print("\nWhat do you want to update?")
            print("1. Name")
            print("2. Email")
            print("3. Department")
            print("4. Position")
            print("5. Salary")
            print("6. Exit")

            try:
                pick = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter a number from 1 to 6.")
                continue

            if pick == 1:
                new_name = input("Enter new employee name: ")
                self.employees[employee_id].employee_name = new_name

            elif pick == 2:
                new_email = input("Enter new employee email: ")
                self.employees[employee_id].gmail = new_email

            elif pick == 3:
                new_department = input("Enter new employee department: ")
                self.employees[employee_id].department = new_department

            elif pick == 4:
                new_position = input("Enter new employee position: ")
                self.employees[employee_id].position = new_position

            elif pick == 5:
                try:
                    new_salary = float(input("Enter new employee salary: "))
                    self.employees[employee_id].salary = new_salary
                except ValueError:
                    print("Salary must be a number.")

            elif pick == 6:
                print("Exit.")
                break

            else:
                print("Invalid choice.")

    def save_employee(self):
        with open("employees.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(headers)

            for employee in self.employees.values():
                writer.writerow([
                    employee.employee_id,
                    employee.employee_name,
                    employee.gmail,
                    employee.department,
                    employee.position,
                    employee.salary
                ])

        print("Employees saved to CSV.")


class Payroll:
    def calculate_monthly_salary(self, employee):
        return float(employee.salary)

    def calculate_yearly_salary(self, employee):
        return float(employee.salary) * 12


class PayrollManager:
    def __init__(self, employee_manager):
        self.employee_manager = employee_manager
        self.payroll = Payroll()

    def show_salary(self):
        try:
            employee_id = int(input("Enter employee ID: "))
        except ValueError:
            print("Employee ID must be a number.")
            return

        if employee_id not in self.employee_manager.employees:
            print("Employee not found.")
            return

        employee = self.employee_manager.employees[employee_id]

        monthly = self.payroll.calculate_monthly_salary(employee)
        yearly = self.payroll.calculate_yearly_salary(employee)

        print("--------------------")
        print("Employee:", employee.employee_name)
        print("Monthly salary:", monthly)
        print("Yearly salary:", yearly)

    def show_department_payroll(self):
        department = input("Enter department: ")

        total = 0
        found = False

        for employee in self.employee_manager.employees.values():
            if employee.department.lower() == department.lower():
                total += float(employee.salary)
                found = True

        if found:
            print("Department:", department)
            print("Total monthly payroll:", total)
            print("Total yearly payroll:", total * 12)
        else:
            print("No employees found in this department.")


employee_manager = EmployeeManager()

try:
    with open("employees.csv", "r", newline="") as file:
        reader = csv.reader(file)

        next(reader, None)

        for row in reader:
            if len(row) != 6:
                print("Skipped invalid CSV row.")
                continue

            try:
                employee_id = int(row[0])
                employee_name = row[1]
                gmail = row[2]
                department = row[3]
                position = row[4]
                salary = float(row[5])

                employee_manager.add_existing_employee(
                    employee_id,
                    employee_name,
                    gmail,
                    department,
                    position,
                    salary
                )

            except ValueError:
                print("Skipped invalid employee data.")

except FileNotFoundError:
    print("employees.csv not found. Starting with an empty employee manager.")


payroll_manager = PayrollManager(employee_manager)


while True:
    print("\n==============================")
    print("Employee Management System")
    print("==============================")
    print("1. Add employee")
    print("2. Show employees")
    print("3. Search employee")
    print("4. Update employee")
    print("5. Remove employee")
    print("6. Show employee salary")
    print("7. Show department payroll")
    print("8. Save")
    print("9. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        name = input("Enter employee name: ")
        gmail = input("Enter employee email: ")
        department = input("Enter department: ")
        position = input("Enter position: ")

        try:
            salary = float(input("Enter salary: "))
        except ValueError:
            print("Salary must be a number.")
            continue

        employee_manager.add_emp(
            name,
            gmail,
            department,
            position,
            salary
        )

    elif choice == 2:
        employee_manager.show_employees()

    elif choice == 3:
        employee_manager.search_employee()

    elif choice == 4:
        employee_manager.update_employee()

    elif choice == 5:
        employee_manager.remove_employee()

    elif choice == 6:
        payroll_manager.show_salary()

    elif choice == 7:
        payroll_manager.show_department_payroll()

    elif choice == 8:
        employee_manager.save_employee()

    elif choice == 9:
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")