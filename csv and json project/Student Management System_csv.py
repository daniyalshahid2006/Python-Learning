import  csv


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
        with open("students.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["Student_id","first_name", "age", "phone"])

            for student_id in self.students:
                student = self.students[student_id]
                writer.writerow([student_id,student.first_name, student.age, student.get_phone()])
    def add_student(self, student_id ,student_name, student_age, student_phone):
        self.students[student_id] = Student(student_name, student_age, student_phone)
    def show_students(self):
        for student_id in self.students:
            print(student_id)
            self.students[student_id].display()
    def search_student(self):
        student_id = input("Enter Student ID: ")
        if student_id in self.students:
            print(student_id)
            self.students[student_id].display()
        else:
            print("Student not found")
    def update_student(self):
        student_id = input("Enter Student ID: ")
        if student_id in self.students:
            pick = ""
            while pick != "4":
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
                    self.students[student_id].age =  new_age
                elif pick == "3":
                    new_phone = input("Enter new phone: ")
                    self.students[student_id].set_phone(new_phone)
        else:
            print("Student not found")

    def delete_student(self):
        student_id = input("Enter Student ID: ")
        if student_id in self.students:
            del self.students[student_id]
            self.save_student()
        else:
            print("Student not found")
    def count_students(self):
        print(f"Student count: {len(self.students)}")
    def bye(self):
        print("Bye")
with open("students.csv","r", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    manager = Manager()
    for row in reader:
        manager.add_student(row[0], row[1], row[2],row[3])
choice = ""

while choice != "7":
    print("Welcome to Student Management System")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Count Students")
    print("7. Bye")

    choice = input("Enter your choice: ")
    if choice == "1":
        id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        phone = input("Enter Student Phone: ")
        manager.add_student(id,name, age, phone)
        manager.save_student()
    elif choice == "2":
        manager.show_students()
    elif choice == "3":
        manager.search_student()
    elif choice == "4":
        manager.update_student()
        manager.save_student()
    elif choice == "5":
        manager.delete_student()
    elif choice == "6":
        manager.count_students()
    elif choice == "7":
        manager.bye()




