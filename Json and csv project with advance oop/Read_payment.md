# Employee Management & Payroll System

A Python-based Employee Management & Payroll System built using **Object-Oriented Programming (OOP)** and **CSV file handling**.

The project allows employees to be added, searched, updated, removed, and stored permanently in a CSV file. It also includes basic payroll calculations and department payroll tracking.

## Features

* Add new employees
* Automatically generate employee IDs
* Reuse available employee IDs
* Display all employees
* Search employees by ID
* Update employee information
* Remove employees
* Save employee data to CSV
* Load employee data from CSV when the program starts
* Calculate monthly salary
* Calculate yearly salary
* Calculate total department payroll
* Handle invalid employee IDs
* Handle invalid menu choices
* Handle invalid salary input
* Skip invalid CSV rows
* Handle missing CSV files

## Employee Information

Each employee contains:

* Employee ID
* Employee Name
* Gmail
* Department
* Position
* Salary

## Technologies Used

* Python
* Object-Oriented Programming
* Classes and Objects
* Dictionaries
* Loops and Conditional Statements
* Exception Handling
* CSV File Handling

## Classes

### `Employee`

Stores information about an individual employee.

### `EmployeeManager`

Responsible for managing employees.

It handles:

* Adding employees
* Loading existing employees
* Searching employees
* Updating employees
* Removing employees
* Displaying employees
* Saving employees to CSV

### `Payroll`

Handles salary calculations.

It calculates:

* Monthly salary
* Yearly salary

### `PayrollManager`

Connects payroll functionality with the `EmployeeManager`.

It handles:

* Showing an employee's salary
* Calculating department payroll

## CSV Persistence

The program uses `employees.csv` to permanently store employee information.

When the program starts:

```text
employees.csv
      ↓
Read CSV
      ↓
Create Employee objects
      ↓
EmployeeManager
```

When the user saves:

```text
EmployeeManager
      ↓
Save employees
      ↓
employees.csv
```

The CSV file contains:

```text
employee_id,employee_name,gmail,department,position,salary
```

## Example CSV Data

```text
employee_id,employee_name,gmail,department,position,salary
1,Daniyal,daniyal@gmail.com,AI,CEO,100000
2,Ahmed,ahmed@gmail.com,AI,Employee,80000
```

## How to Run

1. Make sure Python is installed.
2. Open the project in PyCharm or another Python IDE.
3. Make sure `employees.csv` is in the project folder.
4. Run the Python file.
5. Use the menu to manage employees.

## Sample Run

```text
==============================
Employee Management System
==============================
1. Add employee
2. Show employees
3. Search employee
4. Update employee
5. Remove employee
6. Show employee salary
7. Show department payroll
8. Save
9. Exit

Enter your choice: 1

Enter employee name: Daniyal
Enter employee email: daniyal@gmail.com
Enter department: AI
Enter position: CEO
Enter salary: 100000

Employee added with ID 1
```

### Updating an Employee

```text
Enter your choice: 4

Enter employee ID: 1

What do you want to update?
1. Name
2. Email
3. Department
4. Position
5. Salary
6. Exit

Enter your choice: 5
Enter new employee salary: 150000
```

### Payroll

```text
Enter your choice: 6

Enter employee ID: 1

Employee: Daniyal
Monthly salary: 150000.0
Yearly salary: 1800000.0
```

### Saving

```text
Enter your choice: 8

Employees saved to CSV.
```

After restarting the program, the saved employees are loaded from `employees.csv`.

## Project Learning Goals

This project was created to practice:

* Object-Oriented Programming
* Managing objects using dictionaries
* Reading CSV files
* Writing CSV files
* Converting CSV data into Python objects
* Converting Python objects back into CSV data
* Data persistence
* Updating and deleting persistent data
* Exception handling
* Basic payroll calculations
* Organizing a larger Python project

## Future Improvements

Possible improvements for the project include:

* Stronger email validation
* Better salary validation
* Separate department management
* Payroll history
* Employee attendance
* Login/authentication
* GUI interface
* Database integration

## Author

Daniyal Shahid

Python / AI Student
****