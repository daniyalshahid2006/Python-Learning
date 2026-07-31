import csv
# with open("students.csv","w",newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name","Age","Gmail"])

def Addstudent():
    with open("students.csv", "a", newline="") as file:
        data = csv.writer(file)
        name = input("Enter Student Name :")
        age = input("Enter Age :")
        gmail = input("Enter Gmail :")
        data.writerow([name, age, gmail])
    print("Student Added Successfully")


def showStudent():
    with open("students.csv", "r", newline="") as file:
        data = csv.reader(file)
        next(data)
        for row in data:
            print("student Name :", row[0])
            print("Age :", row[1])
            print("Gmail :", row[2])
            print("_" * 30)
def searchStudent():
    with open("students.csv", "r", newline="") as file:
        data = csv.reader(file)
        next(data)
        search = input("Enter Student Name :")
        for row in data:
            if row[0] == search:
                print("Student Name :", row[0])
                print("Age :", row[1])
                print("Gmail :", row[2])
                return


    print("Student not Found")


def updateStudent():
    with open("students.csv", "r", newline="") as file:
        data = csv.reader(file)
        next(data)
        update = input("Enter Student Name :")
        Rows = []
        found = False
        for row in data:
            Rows.append(row)
        for row in Rows:
            if row[0] == update:
                found = True
                print("1.name")
                print("2.age")
                print("3.gmail")
                pick = input("Enter your choice :")
                if pick == "1":
                    new_name = input("Enter New Student Name :")
                    row[0] = new_name
                elif pick == "2":
                    new_age = input("Enter New Student Age :")
                    row[1] = new_age
                elif pick == "3":
                    new_gmail = input("Enter New Student Gmail :")
                    row[2] = new_gmail
                else:
                    print("Invalid Choice")
                break


    if found:
     with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(Rows)
     print("Student Updated Successfully")
    else:
        print("Student not Found")
def deleteStudent():
    with open ("students.csv","r",newline="") as file:
        data = csv.reader(file)
        next(data)
        delete = input("Enter Student Name :")
        Rows = []
        found = False
        for row in data:
            Rows.append(row)
        for row in Rows:
            if row[0] == delete:
                found = True
                Rows.remove(row)
                break
    if found:
        with open("students.csv","w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(Rows)
            print("Student Deleted Successfully")
    else:
        print("Student not Found")

def countStudents():
    with open ("students.csv","r",newline="") as file:
        data = csv.reader(file)
        next(data)
        count = 0
        for row in data:
            count += 1
    print("Total Students:", count)
def bye():
    print("Bye")
choice =""
while choice != "7":
    print("1. Add Student")
    print("2. show Student")
    print("3. search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. count Students")
    print("7. Exit")
    choice = input("Enter your choice :")
    if choice == "1":
        Addstudent()
    elif choice == "2":
        showStudent()
    elif choice == "3":
        searchStudent()
    elif choice == "4":
        updateStudent()
    elif choice == "5":
        deleteStudent()
    elif choice == "6":
        countStudents()
    elif choice == "7":
        bye()
    else:
        print("Invalid Choice")
    