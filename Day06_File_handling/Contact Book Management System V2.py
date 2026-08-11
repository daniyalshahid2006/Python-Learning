import json


with open("contacts.json", "r") as file:
    data = json.load(file)


def SaveContact():
    with open("contacts.json", "w") as file:
        json.dump(data, file,indent=4)



def AddContact():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    skills = {}
    while True:
        pick = input("Do you want to add another contact? (y/n): ").lower()
        if pick == "y":
            Skill_name = input("Enter your Skill name: ")
            skill_lvl = input("Enter your Skill level: ")
            skills[Skill_name] = skill_lvl
        else:
            break
    data[name] = {
        "email": email,
        "phone": phone,
        "skills": skills
    }
    SaveContact()
    print("Added successfully!")

def showContact():
    for name in data:
        print("_" * 30)
        print(f"Name : {name}")
        print(f"Email : {data[name]['email']}")
        print(F"phone number : {data[name]['phone']}")
        print("skills:")
        for skill in data[name]['skills']:
            print(f"- {skill}:{data[name]['skills'][skill]}")

    print("_" * 30)


def searchContact():
    name_search = input("Enter name: ")
    if name_search in data:
        print("_" * 30)
        print(f"Name : {name_search}")
        print(f"Email : {data[name_search]['email']}")
        print(f"Phone number : {data[name_search]['phone']}")
        print("skills:")
        for skill in data[name_search]['skills']:
            print(f"- {skill}:{data[name_search]['skills'][skill]}")

        print("_" * 30)

    else:
        print("contact not found")


def UpdateContact():
    upd = input("who do  you want to update?")
    if upd in data:
        print("1.name")
        print("2.email")
        print("3.phone")
        print("4.skills")
        pick = input("what do you want to update?")
        if pick == "1":
            name_update = input("Enter your name: ")
            info = data.pop(upd)
            data[name_update] = info
        elif pick == "2":
            data[upd]["email"] = input("Enter your email: ")
        elif pick == "3":
            data[upd]["phone"] = input("Enter your phone number: ")
        elif pick == "4":
            skill_update = input("Enter your Skill name: ")
            skill_lvl_update = input("Enter your Skill level: ")
            if skill_update in data[upd]["skills"]:
                data[upd]["skills"][skill_update] = skill_lvl_update
            else:
                print("skill not found")
                return
        else:
            print("invalid input")
            return
    else:
        print("contact not found")
        return
    SaveContact()
    print("Updated successfully!")


def deleteContact():
    delete_name = input("who do you want to delete?")
    if delete_name in data:
        data.pop(delete_name)
        SaveContact()
        print("Deleted successfully!")
    else:
     print("contact not found")
    return
def countContact():
    print("total contacts :", len(data))
def bye():
    print("bye")
    exit()
option = ""
while option != "7":
    print("1. Add contact")
    print("2.show contact")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6.count contact")
    print("7. Exit")
    option = input("Enter your choice: ")
    if option == "1":
        AddContact()
    elif option == "2":
        showContact()
    elif option == "3":
        searchContact()
    elif option == "4":
        UpdateContact()
    elif option == "5":
        deleteContact()
    elif option == "6":
        countContact()
    elif option == "7":
        bye()
    else:
     print("invalid input")