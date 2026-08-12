# Student Management System

A console-based Student Management System built with Python using Object-Oriented Programming (OOP) and JSON for data storage.

## Features

* Add a student
* Display all students
* Search for a student by ID
* Update student information
* Delete a student
* Count total students
* Automatically save changes to a JSON file
* Load existing students when the program starts

## Concepts Used

* Classes and Objects
* Encapsulation
* Private attributes
* Getter and Setter methods
* Dictionaries
* Functions and Methods
* Loops and Conditional Statements
* User Input
* File Handling
* JSON
* CRUD operations

## How It Works

Students are stored in a dictionary where the **student ID is the key** and the **Student object is the value**.

The program uses `students.json` to permanently store student information.

When the program starts:

1. The JSON file is loaded.
2. Student data is converted into `Student` objects.
3. The objects are stored inside the `Manager`.
4. The user can interact with the system through the menu.
5. Changes are saved back to `students.json`.

## Menu

```text
Welcome to Student Management System
1. Add Student
2. Show Student
3. Search Student
4. Update Student
5. Delete Student
6. Count Students
7. Bye
```

## Sample Run

```text
Welcome to Student Management System
1. Add Student
2. Show Student
3. Search Student
4. Update Student
5. Delete Student
6. Count Students
7. Bye

Enter your choice: 1
Enter student ID: 4
Enter student name: Dani
Enter student email: dani@gmail.com
Enter student phone: 03001234567

Enter your choice: 2
1
John
john@gmail.com
03001111111

2
Mike
mike@gmail.com
03002222222

4
Dani
dani@gmail.com
03001234567

Enter your choice: 3
Enter student ID: 4
Dani
dani@gmail.com
03001234567

Enter your choice: 6
There are 3 students

Enter your choice: 7
Bye
```

## Project Structure

```text
Student Management System.py
students.json
README.md
```

## Technologies

* Python
* JSON
* Object-Oriented Programming
* File Handling
