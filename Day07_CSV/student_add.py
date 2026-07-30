import csv

with open("students.csv","a",newline="") as file:
    data = csv.writer(file)
    name = input("Enter Student Name :")
    age = input("Enter Student Age :")
    subject = input("Enter Student Subject :")
    data.writerow([name,age,subject])
    print("Student Added Successfully")

with open("students.csv","r")  as file:
        data = csv.reader(file)
        for row in data:
            print(row)