# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from random import choice

Choice = choice
while Choice != "5":
 print("===== MENU =====")
 print("1. Enter Student")
 print("2. Show Student")
 print("3. Check Grade")
 print("4. Multiplication Table")
 print("5. Exit")
 choice = input("Enter your choice:(1/2/3/4/5)")
 if choice == "1":
    student = input("Enter your name:")
    student_age = int(input("Enter your age:"))
    student_marks = int(input("Enter your marks:"))
