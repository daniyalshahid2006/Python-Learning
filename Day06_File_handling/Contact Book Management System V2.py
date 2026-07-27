import json

with open("contacts.json") as file:
    contacts = json.load(file)


def SaveContacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)


def AddContacts():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    skills = {}
    while True:
        pick = input("Do you have skill (y/n): ").lower()
        if pick == "n":
            break
        else:
            skill_name = input("Enter your skill name: ")
            skill_level = input("Enter your skill level: ")
            skills[skill_name] = skill_level
    contacts[name] = {
        "email": email,
        "phone": phone,
        "skills": skills
    }
    SaveContacts()

    print("Contact added successfully")
