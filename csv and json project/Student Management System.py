import json



class Student:
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.__phone = phone
    def display(self):
        print(self.name)
        print(self.email)
        print(self.__phone)
    def get_phone(self):
        return self.__phone
    def set_phone(self,new_phone):
        self.__phone = new_phone
class Manager:
    def __init__(self):
        self.students = {}
    def add_student(self,student_id,student_name,student_email,student_phone):
        self.students[student_id] = Student(student_name,student_email,student_phone)
        self.save_student()
    def show_students(self):
        for student in self.students:
            print(student)
            self.students[student].display()
    def search_student(self,student_id):
        if student_id in self.students:
         self.students[student_id].display()
        else:
            print("Student does not exist")
    def save_student(self):
        data = {}
        for student_id in self.students:
            student = self.students[student_id]
            data[student_id] ={
                "name" : student.name,
                "email" : student.email,
                "phone" : student.get_phone()
            }
        with open("students.json", "w") as file:
            json.dump(data, file,indent=4)
    def update_student(self):
        name_upd = input("who do you want to update? ")
        if name_upd in self.students:
            print("1.name")
            print("2.email")
            print("3.phone")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                new_name = input("Enter new student name: ")
                self.students[name_upd].name = new_name
            elif choice == 2:
                new_mail = input("Enter new student email: ")
                self.students[name_upd].email = new_mail
            elif choice == 3:
                new_phone = input("Enter new student phone: ")
                self.students[name_upd].set_phone(new_phone)
            else:
                print("Invalid choice")
            self.save_student()
        else:
            print("student does not exist")
    def delete_student(self):
        name_del = input("Enter student name to delete? ")
        if name_del in self.students:
            del self.students[name_del]
            self.save_student()
        else:
            print("student does not exist")
    def count_students(self):
       count =  len(self.students)
       print("There are ",count,"students")
    def bye(self):
        print("Bye")




with open ("students.json","r") as file:
    data = json.load(file)
manager = Manager()
for student_id in data:
    manager.add_student(
        student_id,
        data[student_id]["name"],
        data[student_id]["email"],
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
        Student_id = int(input("Enter student ID: "))
        Student_name = input("Enter student name: ")
        Student_email = input("Enter student email: ")
        Student_phone = input("Enter student phone: ")
        manager.add_student(Student_id,Student_name,Student_email,Student_phone)
    elif choice == "2":
        manager.show_students()
    elif choice == "3":
        search_id = int(input("Enter student ID: "))
        manager.search_student(search_id)
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

