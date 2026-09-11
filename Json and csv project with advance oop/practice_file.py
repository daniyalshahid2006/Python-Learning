
import csv


# ============================================================
# CSV HEADER
# ============================================================

headers = ["student_id", "name", "email", "department", "marks"]


# ============================================================
# STUDENT CLASS
# ============================================================

class Student:

    def __init__(self, student_id, name, email, department, marks):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.department = department
        self.marks = marks


# ============================================================
# STUDENT MANAGER
# ============================================================

class StudentManager:

    def __init__(self):
        # Dictionary:
        # key   = student ID
        # value = Student object
        self.students = {}


    # ========================================================
    # ADD NEW STUDENT
    # ========================================================

    def add_student(self):

        name = input("Enter student name: ")
        email = input("Enter student email: ")
        department = input("Enter department: ")

        try:
            marks = float(input("Enter marks: "))

        except ValueError:
            print("Marks must be a number.")
            return

        # Find the first available ID
        candidate = 1

        while candidate in self.students:
            candidate += 1

        # Create Student object
        student = Student(
            candidate,
            name,
            email,
            department,
            marks
        )

        # Store object inside dictionary
        self.students[candidate] = student

        print("Student added with ID:", candidate)


    # ========================================================
    # SHOW ALL STUDENTS
    # ========================================================

    def show_students(self):

        if not self.students:
            print("No students found.")
            return

        # .values() gives Student objects
        for student in self.students.values():

            print("\n--------------------")
            print("ID:", student.student_id)
            print("Name:", student.name)
            print("Email:", student.email)
            print("Department:", student.department)
            print("Marks:", student.marks)


    # ========================================================
    # SEARCH STUDENT
    # ========================================================

    def search_student(self):

        try:
            student_id = int(input("Enter student ID: "))

        except ValueError:
            print("ID must be a number.")
            return

        # Check if ID exists in dictionary
        if student_id in self.students:

            # Get Student object
            student = self.students[student_id]

            print("\n--------------------")
            print("ID:", student.student_id)
            print("Name:", student.name)
            print("Email:", student.email)
            print("Department:", student.department)
            print("Marks:", student.marks)

        else:
            print("Student not found.")


    # ========================================================
    # UPDATE STUDENT
    # ========================================================

    def update_student(self):

        try:
            student_id = int(input("Enter student ID: "))

        except ValueError:
            print("ID must be a number.")
            return

        if student_id not in self.students:
            print("Student not found.")
            return

        while True:

            print("\nWhat do you want to update?")
            print("1. Name")
            print("2. Email")
            print("3. Department")
            print("4. Marks")
            print("5. Exit")

            try:
                choice = int(input("Enter your choice: "))

            except ValueError:
                print("Enter a number.")
                continue


            if choice == 1:

                new_name = input("Enter new name: ")

                self.students[student_id].name = new_name

                print("Name updated.")


            elif choice == 2:

                new_email = input("Enter new email: ")

                self.students[student_id].email = new_email

                print("Email updated.")


            elif choice == 3:

                new_department = input("Enter new department: ")

                self.students[student_id].department = new_department

                print("Department updated.")


            elif choice == 4:

                try:
                    new_marks = float(
                        input("Enter new marks: ")
                    )

                    self.students[student_id].marks = new_marks

                    print("Marks updated.")

                except ValueError:
                    print("Marks must be a number.")


            elif choice == 5:

                print("Finished updating.")
                break


            else:

                print("Invalid choice.")


    # ========================================================
    # REMOVE STUDENT
    # ========================================================

    def remove_student(self):

        try:
            student_id = int(
                input("Enter student ID to remove: ")
            )

        except ValueError:
            print("ID must be a number.")
            return

        if student_id in self.students:

            # Delete student from dictionary
            del self.students[student_id]

            print("Student removed.")

        else:

            print("Student not found.")


    # ========================================================
    # CALCULATE AVERAGE
    # ========================================================

    def calculate_average(self):

        if not self.students:
            print("No students found.")
            return

        total = 0

        # Go through every Student object
        for student in self.students.values():

            total += student.marks

        average = total / len(self.students)

        print("Average marks:", average)


    # ========================================================
    # SHOW DEPARTMENT STUDENTS
    # ========================================================

    def show_department(self):

        department = input("Enter department: ")

        found = False

        for student in self.students.values():

            if student.department.lower() == department.lower():

                print("--------------------")
                print("ID:", student.student_id)
                print("Name:", student.name)
                print("Email:", student.email)
                print("Marks:", student.marks)

                found = True

        if not found:
            print("No students found in this department.")


    # ========================================================
    # SHOW DICTIONARY USING .ITEMS()
    # ========================================================

    def show_dictionary_items(self):

        # .items() gives both key and value
        for student_id, student in self.students.items():

            print(
                "Dictionary key:",
                student_id,
                "| Student:",
                student.name
            )


    # ========================================================
    # SAVE TO CSV
    # ========================================================

    def save_students(self):

        # "w" clears the old file and writes current data
        with open(
            "students.csv",
            "w",
            newline=""
        ) as file:

            writer = csv.writer(file)

            # Write header
            writer.writerow(headers)

            # Write every Student object
            for student in self.students.values():

                writer.writerow([
                    student.student_id,
                    student.name,
                    student.email,
                    student.department,
                    student.marks
                ])

        print("Students saved to CSV.")


# ============================================================
# CREATE MANAGER
# ============================================================

student_manager = StudentManager()


# ============================================================
# LOAD EXISTING STUDENTS FROM CSV
# ============================================================

try:

    with open(
        "students.csv",
        "r",
        newline=""
    ) as file:

        # Create CSV reader
        reader = csv.reader(file)

        # Skip header
        next(reader, None)

        # Read every row
        for row in reader:

            # Make sure row contains all required values
            if len(row) != 5:
                print("Skipped invalid CSV row.")
                continue

            try:

                # CSV values start as strings
                student_id = int(row[0])
                name = row[1]
                email = row[2]
                department = row[3]
                marks = float(row[4])

                # Create object from CSV data
                student = Student(
                    student_id,
                    name,
                    email,
                    department,
                    marks
                )

                # Store object in dictionary
                student_manager.students[student_id] = student

            except ValueError:

                print("Skipped invalid student data.")


except FileNotFoundError:

    print("students.csv not found.")
    print("Starting with an empty student manager.")


# ============================================================
# MAIN MENU
# ============================================================

while True:

    print("\n================================")
    print("      STUDENT MANAGEMENT")
    print("================================")

    print("1. Add student")
    print("2. Show students")
    print("3. Search student")
    print("4. Update student")
    print("5. Remove student")
    print("6. Calculate average")
    print("7. Show department students")
    print("8. Show dictionary items")
    print("9. Save to CSV")
    print("10. Exit")


    # Get menu choice
    try:

        choice = int(
            input("Enter your choice: ")
        )

    except ValueError:

        print("Please enter a number.")
        continue


    # ========================================================
    # MENU OPTIONS
    # ========================================================

    if choice == 1:

        student_manager.add_student()


    elif choice == 2:

        student_manager.show_students()


    elif choice == 3:

        student_manager.search_student()


    elif choice == 4:

        student_manager.update_student()


    elif choice == 5:

        student_manager.remove_student()


    elif choice == 6:

        student_manager.calculate_average()


    elif choice == 7:

        student_manager.show_department()


    elif choice == 8:

        student_manager.show_dictionary_items()


    elif choice == 9:

        student_manager.save_students()


    elif choice == 10:

        print("Goodbye.")
        break


    else:

        print("Invalid choice.")