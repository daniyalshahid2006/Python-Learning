import csv
import os

HEADERS = ["employee_id", "employee_name", "gmail", "department", "position", "salary"]
CSV_FILE = "employees.csv"


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
            print("Employee already exists, change id")
        else:
            employee = Employee(employee_id, employee_name, gmail, department, position, salary)
            self.employees[employee_id] = employee

    def add_emp(self, employee_name, gmail, department, position, salary):
        candidate = 1
        while candidate in self.employees:
            candidate = candidate + 1
        employee = Employee(candidate, employee_name, gmail, department, position, salary)
        self.employees[candidate] = employee
        print(f"Employee added with id {candidate}")

    def show_employees(self):
        if not self.employees:
            print("No employees to show.")
            return
        print(f"{'ID':<6}{'Name':<20}{'Email':<25}{'Department':<15}{'Position':<15}{'Salary':<10}")
        print("-" * 91)
        for employee in self.employees.values():
            print(f"{employee.employee_id:<6}{employee.employee_name:<20}{employee.gmail:<25}"
                  f"{employee.department:<15}{employee.position:<15}{employee.salary:<10}")

    def search_employee(self):
        try:
            search_id = int(input("Enter employee id: "))
        except ValueError:
            print("Invalid input. Employee id must be a number.")
            return
        if search_id in self.employees:
            emp = self.employees[search_id]
            print(emp.employee_name)
            print(emp.gmail)
            print(emp.department)
            print(emp.position)
            print(emp.salary)
        else:
            print("Employee not found")

    def remove_employee(self):
        try:
            search_id = int(input("Enter employee id you want to remove: "))
        except ValueError:
            print("Invalid input. Employee id must be a number.")
            return
        if search_id in self.employees:
            del self.employees[search_id]
            print("Employee removed")
        else:
            print("Employee not found")

    def save_employee(self):
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)
            for employee in self.employees.values():
                writer.writerow([employee.employee_id, employee.employee_name, employee.gmail,
                                  employee.department, employee.position, employee.salary])
        print("Employees saved to file.")

    def update_employee(self):
        try:
            id = int(input("Enter employee id: "))
        except ValueError:
            print("Invalid input. Employee id must be a number.")
            return
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
                try:
                    pick = int(input("Enter your choice: "))
                except ValueError:
                    print("Invalid choice, enter a number 1-6.")
                    continue
                if pick == 1:
                    new_name = input("Enter new employee name: ")
                    self.employees[id].employee_name = new_name
                elif pick == 2:
                    new_email = input("Enter new employee email: ")
                    if "@" not in new_email:
                        print("Invalid email, must contain '@'.")
                        continue
                    self.employees[id].gmail = new_email
                elif pick == 3:
                    new_department = input("Enter new employee department: ")
                    self.employees[id].department = new_department
                elif pick == 4:
                    new_position = input("Enter new employee position: ")
                    self.employees[id].position = new_position
                elif pick == 5:
                    new_salary = input("Enter new employee salary: ")
                    try:
                        new_salary = float(new_salary)
                        if new_salary < 0:
                            print("Salary cannot be negative.")
                            continue
                    except ValueError:
                        print("Invalid salary, must be a number.")
                        continue
                    self.employees[id].salary = new_salary
                elif pick == 6:
                    print("exit")
                else:
                    print("Invalid choice, pick between 1 and 6.")

    # ---- Payroll / department reporting ----
    def calculate_total_payroll(self):
        total = 0
        for employee in self.employees.values():
            try:
                total += float(employee.salary)
            except (TypeError, ValueError):
                continue
        return total

    def calculate_average_salary(self):
        if not self.employees:
            return 0
        return self.calculate_total_payroll() / len(self.employees)

    def employees_by_department(self, department):
        return [emp for emp in self.employees.values() if emp.department.lower() == department.lower()]

    def department_payroll(self, department):
        total = 0
        for emp in self.employees_by_department(department):
            try:
                total += float(emp.salary)
            except (TypeError, ValueError):
                continue
        return total

    def show_payroll_report(self):
        if not self.employees:
            print("No employees to report on.")
            return
        departments = sorted(set(emp.department for emp in self.employees.values()))
        print("=== Payroll Report ===")
        for dept in departments:
            dept_total = self.department_payroll(dept)
            dept_count = len(self.employees_by_department(dept))
            print(f"{dept}: {dept_count} employee(s), total salary = {dept_total:.2f}")
        print("-" * 30)
        print(f"Total monthly payroll: {self.calculate_total_payroll():.2f}")
        print(f"Total annual payroll: {self.calculate_total_payroll() * 12:.2f}")
        print(f"Average salary: {self.calculate_average_salary():.2f}")


def load_employees(manager):
    if not os.path.exists(CSV_FILE):
        print("No existing employee file found, starting fresh.")
        return
    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)
        try:
            next(reader)
        except StopIteration:
            return
        for row in reader:
            if len(row) != 6:
                print(f"Skipping malformed row: {row}")
                continue
            try:
                employee_id = int(row[0])
                employee_name = row[1]
                gmail = row[2]
                department = row[3]
                position = row[4]
                salary = float(row[5])
            except ValueError:
                print(f"Skipping row with bad data: {row}")
                continue
            manager.add_existing_employee(employee_id, employee_name, gmail, department, position, salary)


def main():
    employee_manager = EmployeeManager()
    load_employees(employee_manager)

    while True:
        print("\n===== Employee Management Menu =====")
        print("1. Add employee")
        print("2. Show all employees")
        print("3. Search employee")
        print("4. Update employee")
        print("5. Remove employee")
        print("6. Save employees")
        print("7. Payroll report")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter employee name: ")
            email = input("Enter employee email: ")
            department = input("Enter employee department: ")
            position = input("Enter employee position: ")
            try:
                salary = float(input("Enter employee salary: "))
            except ValueError:
                print("Invalid salary, must be a number. Employee not added.")
                continue
            employee_manager.add_emp(name, email, department, position, salary)
        elif choice == "2":
            employee_manager.show_employees()
        elif choice == "3":
            employee_manager.search_employee()
        elif choice == "4":
            employee_manager.update_employee()
        elif choice == "5":
            employee_manager.remove_employee()
        elif choice == "6":
            employee_manager.save_employee()
        elif choice == "7":
            employee_manager.show_payroll_report()
        elif choice == "8":
            employee_manager.save_employee()
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()