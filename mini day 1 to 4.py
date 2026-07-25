student_name = ""
student_age = 0
student_marks = 0
choice = ""
while choice != "5":
 print("===== MENU =====")
 print("1. Enter Student")
 print("2. Show Student")
 print("3. Check Grade")
 print("4. Multiplication Table")
 print("5. Exit")
 choice = input("Enter your choice:(1/2/3/4/5)")
 if choice == "1":
    student_name = input("Enter your name:")
    student_age = int(input("Enter your age:"))
    student_marks = int(input("Enter your marks:"))
 elif choice == "2":
  print(student_name, student_age, student_marks)
 elif choice == "3":
    if student_marks >= 90:
        print("A")
    elif student_marks >= 80:
        print("B")
    elif student_marks >= 70:
        print("C")
    elif student_marks >= 60:
        print("D")
    elif student_marks >= 50:
        print("E")
    else:
        print("F")

 elif choice == "4":
    num = int(input("Enter your number:"))
    for i in range(1,11):
        print(num, "*", i, "=", num*i)
 elif choice == "5":
     print("good bye")
