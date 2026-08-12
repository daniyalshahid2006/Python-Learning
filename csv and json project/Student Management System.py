import json


class Student:
    def __init__(self, first_name, age, phone):
        self.first_name = first_name
        self.age = age
        self.__phone = phone

    def display(self):
        print(self.first_name)
        print(self.age)
        print(self.__phone)

    def get_phone(self):
        return self.__phone

    def set_phone(self, new_phone):
        self.__phone = new_phone


class Manager:
    def __init__(self):
        self.students = {}

    def save_student(self):
        data = {}
        for student_id in self.students:
            student = self.students[student_id]
            data[student_id] = {
                "name": student.first_name,
                "age": student.age,
                "phone": student.get_phone()
            }
        with open("students.json", "w") as file:
            json.dump(data, file, indent=4)

    def add_student(self, student_id, student_name, student_age, student_phone):
        self.students[student_id] = Student(student_name, student_age, student_phone)

    def show_students(self):
        for student_id in self.students:
            print(student_id)
            self.students[student_id].display()

    def select_student(self):
        student_id = input("Enter student id: ")
        if student_id in self.students:
            self.students[student_id].display()
        else:
            print("Student not found")

    def update_student(self):
        student_id = input("Enter student id: ")
        if student_id in self.students:
            pick = ""
            while pick != "4":
                print("Select option:")
                print("1.name")
                print("2.age")
                print("3.phone")
                print("4.done")
                pick = input("Enter your choice: ")
                if pick == "1":
                    new_name = input("Enter new name: ")
                    self.students[student_id].first_name = new_name
                elif pick == "2":
                    new_age = input("Enter new age: ")
                    self.students[student_id].age = new_age
                elif pick == "3":
                    new_phone = input("Enter new phone: ")
                    self.students[student_id].set_phone(new_phone)
            self.save_student()
        else:
            print("Student not found")

    def delete_student(self):
        student_id = input("Enter student id: ")
        if student_id in self.students:
            del self.students[student_id]
            self.save_student()

    def count_students(self):
        print(f"student count: {len(self.students)}")

    def bye(self):
        print("Bye")


with open("students.json", "r") as file:
    data = json.load(file)

    manager = Manager()
    for student_id in data:
        manager.add_student(
            student_id,
            data[student_id]["name"],
            data[student_id]["age"],
            data[student_id]["phone"]
        )
choice = ""
while choice != "7":
    print("Welcome to Student Management System")
    print("1.Add Student")
    print("2.Show Student")
    print("3.search Student")
    print("4.update Student")
    print("5.Delete Student")
    print("6.count Students")
    print("7.Bye")
    choice = input("Enter your choice: ")
    if choice == "1":
        Student_id = input("Enter student ID: ")
        Student_name = input("Enter student name: ")
        Student_email = input("Enter student email: ")
        Student_phone = input("Enter student phone: ")
        manager.add_student(Student_id, Student_name, Student_email, Student_phone)
        manager.save_student()
    elif choice == "2":
        manager.show_students()
    elif choice == "3":
        manager.select_student()
    elif choice == "4":
        manager.update_student()
    elif choice == "5":
        manager.delete_student()
    elif choice == "6":
        manager.count_students()
    elif choice == "7":
        manager.bye()
    else:
        print("Invalid choice")
