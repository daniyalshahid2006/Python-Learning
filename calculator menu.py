def Add():
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    return num1 + num2
def sub():
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
def exit():
    print("bye")

choice = ""
while choice != "5":
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        result = Add()
        print(result)
    elif choice == "2":
        result = sub()
        print(result)
    elif choice == "3":
        num1 = int(input("enter first number: "))
        num2 = int(input("enter second number: "))
        result = multiply(num1, num2)
        print(result)
    elif choice == "4":
        num1 = int(input("enter first number: "))
        num2 = int(input("enter second number: "))
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
         result = divide(num1, num2)
         print(result)

    elif choice == "5":
        exit()
    else:
        print("nooo")