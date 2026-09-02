from pip._internal.models import candidate


class Employee:
    def __init__(self,employee_id,employee_name,gmail,department,position,salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.gmail = gmail
        self.department = department
        self.position = position
        self.salary = salary
class EmployeeManager:
    def __init__(self):
        self.employees = {}
    def add_emp(self,employee_name,gmail,department,position,salary):
        candidate = 1
        while candidate in self.employees:
            candidate = candidate + 1
        employee = Employee(candidate,employee_name,gmail,department,position,salary)
        self.employees[candidate]=employee

employee_manager = EmployeeManager()
employee_manager.add_emp("ali","GMAIL","Department","position","Salary")
print(employee_manager.employees[1].gmail)
