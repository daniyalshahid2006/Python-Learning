student_list = []


def Add_student(student_list):
    add_stu = input("Enter Student Name: ")
    student_list.append(add_stu)
    print("Student Added Successfully")


def show_student(student_list):
    if student_list == []:
        print("Student Not Found")
    else:
        number = 1
        for stu in student_list:
            print(f"{number}. {stu}")
            number += 1


def search_student(student_list):
    if student_list == []:
        print("list is empty")
    else:
        student_search = input("Enter Student Name: ")
        found = False
        for stu in student_list:
            if stu == student_search:
                found = True
                break

        if found:
            print(f"{student_search}")
            print("Student Found")
        else:
            print("Student Not Found")


def delete_student(student_list):
    if student_list == []:
        print("list is empty")
    else:
        student_delete = input("Enter Student Name: ")
        foundd = False
        for stu in student_list:
            if stu == student_delete:
                foundd = True
                break
        if foundd:
            student_list.remove(student_delete)
            print("Student Deleted Successfully")
        else:
          print("Student Not Found")


def count_students(student_list):
    count = len(student_list)
    return count


def bye():
    print("Goodbye")


choice = ""
while choice != "6":
    print("1.Add Student")
    print("2.show Student")
    print("3.Search Student")
    print("4.Delete Student")
    print("5.count Students")
    print("6.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        Add_student(student_list)
    elif choice == "2":
        show_student(student_list)
    elif choice == "3":
        search_student(student_list)
    elif choice == "4":
        delete_student(student_list)
    elif choice == "5":
        find = count_students(student_list)
        print(f"{find} Students Found")
    elif choice == "6":
        bye()
