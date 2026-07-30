import csv
with open("students.csv","r") as file:
    data=csv.reader(file)
    next(data)
    for row in data:
       print(f"Name :{row[0]} Student age :{row[1]} subject :{row[2]}")

