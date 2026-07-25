# students =["aldi","abdu",'dabni']
# print(students[0])
# print(students[2])
# students[1] = "alo"
# print(students[1])
# students.append("yoo yooo")
# print(students[3])
# game = ["aloo","gobi","shobi"]
# game.remove("aloo")
# print(game)
# print(len(game))
# books = ["bla","fla","kalaa"]
# for b in books:
#     print(b)
shooping_list = []
def show_item(shooping_list):
    check = len(shooping_list)
    numbers = 1
    if check != 0:
        for items in shooping_list:
         print(numbers, items)
         numbers = numbers + 1
    else:
        print("nothing")
def add_item(shooping_list):
    item = input("Enter Item: ")
    shooping_list.append(item)
    print(shooping_list)
def remove_item(shooping_list):
        rem = input("Enter Item: ")
        if rem not in shooping_list:
            print("nothing")
        else:
            shooping_list.remove(rem)
            print(shooping_list)
def count_item(shooping_list):
    return len(shooping_list)
def clear_shooping_list(shooping_list):
    shooping_list.clear()
    print(shooping_list)
def bye():
    print("byee")
choice = ""
while choice != "6":
    print("1. show Item")
    print("2. add Item")
    print("3. remove Item")
    print("4. count Item")
    print("5.clear Item")
    print("6. exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        show_item(shooping_list)
    elif choice == "2":
        add_item(shooping_list)
    elif choice == "3":
        remove_item(shooping_list)
    elif choice == "4":
        count = count_item(shooping_list)
        print(count)
    elif choice == "5":
        clear_shooping_list(shooping_list)
    elif choice == "6":
        bye()





