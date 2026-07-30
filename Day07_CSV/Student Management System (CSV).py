import csv


def Addstudent():
    with open("students.csv", "a", newline="") as file:
        data = csv.writer(file)
        name = input("Enter Student Name :")
        age = input("Enter Age :")
        gmail = input("Enter Gmail :")
        data.writerow([name, age, gmail])
    print("Student Added Successfully")


def shwowStudent():
    with open("students.csv", "r", newline="") as file:
        data = csv.reader(file)
        for row in data:
            print(row)


def searchStudent():
    with open("students.csv", "r", newline="") as file:
        data = csv.reader(file)
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
