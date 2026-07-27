contacts = {
}


def AddContact():
    name = input("What is your favorite contact name? ")
    if name in contacts:
        print("name already exists")
        return 
    email = input("What is your favorite contact email? ")
    phone = input("What is your favorite contact phone? ")
    city = input("What is your favorite contact city? ")

    contacts[name] = {
        "email": email,
        "phone": phone,
        "city": city,
    }
    print(f"{name} added successfully")


def Show_All_Contacts():
    if contacts == {}:
        print("No contacts found")
    else:
        for key, value in contacts.items():
            print(f"Name: {key}")
            for info_key, info_value in value.items():
                print(f"{info_key}: {info_value}")
            print("------------------------")


def search_contact():
    search_name = input("Who you want to search? ")
    if search_name in contacts:
        print(f"name: {search_name}")
        for key, value in contacts[search_name].items():
            print(f"{key}: {value}")
    else:
        print("not found")


def update_contact():
    search_name1 = input("Who you want to update? ")
    if search_name1 in contacts:
        upd = input("What you want to update? ")
        if upd in contacts[search_name1]:
            new_value = input("enter value ")

            contacts[search_name1][upd] = new_value
            print(f"{search_name1} updated successfully")
        else:
            print("not found")
    else:
        print("name not found")


def delete_contact():
    if contacts == {}:
        print("dict is empty")
    else:
        search_name = input("Who you want to delete? ")
        if search_name in contacts:
            contacts.pop(search_name)
            print("deleted")
        else:
            print("not found")


def count_contacts():
    if not contacts:
        print("dict is empty")
    print("number of contacts", len(contacts))


def bye():
    print("bye")


choice = ""
while choice != "7":
    print("Welcome to the contact book management system")
    print("1. Add contact")
    print("2. Show all contacts")
    print("3. search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. count contacts")
    print("7. bye")
    choice = input("Enter your choice: ")
    if choice == "1":
        AddContact()
    elif choice == "2":
        Show_All_Contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        count_contacts()
    elif choice == "7":
        bye()
        break
