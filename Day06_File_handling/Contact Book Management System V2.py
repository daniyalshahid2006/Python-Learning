import json

with open('contacts.json', 'r') as file:
    data = json.load(file)


def save_contact():
    with open('contacts.json', 'w') as file:
        json.dump(data, file, indent=4)


def AddContact():
    name = input("What is your name? ")
    email = input("What is your email? ")
    phone = input("What is your phone number? ")
    skills = {}
    while True:
        pick = input("Would you like to add a skill? (y/n) ")
        if pick == "y":
            skill_name = input("What is your favorite skill? ")
            skill_lvl = input("What is your favorite level? ")
            skills[skill_name] = skill_lvl
        else:
            break
    data[name] = {
        "email": email,
        "phone": phone,
        "skills": skills
    }
    save_contact()
    print("Contact added successfully")


def show_contact():
    for name in data:
        print(f"Name: {name}")
        print(f"Email: {data[name]['email']}")
        print(f"phone: {data[name]['phone']}")
        print("Skill Levels:")
        for skill in data[name]['skills']:
            print(f"{skill}: {data[name]['skills'][skill]}")

        print("_" * 30)


def search_contact():
    search_name = input("Who you want to search? ")
    if search_name in data:
        print(f"name: {search_name}")
        print(f"email: {data[search_name]['email']}")
        print(f"phone: {data[search_name]['phone']}")
        print("skills:")
        for skill in data[search_name]['skills']:
            print(f"{skill} : {data[search_name]['skills'][skill]}")
    else:
        print("not found")


print("_" * 30)


def update_contact():
    update_name = input("Who you want to update? ")
    if update_name in data:
        print("what do you want to update? ?")
        print("1.name")
        print("2.email")
        print("3.phone")
        print("4.skills")
        print("_" * 30)
        pick = input("pick one")
        if pick == "1":
            name = input("What is your name? ")
            info = data.pop(update_name)
            data[name] = info
        elif pick == "2":
            email = input("What is your email? ")
            data[update_name]["email"] = email
        elif pick == "3":
            phone = input("What is your phone number? ")
            data[update_name]["phone"] = phone

        elif pick == "4":
            skills_change = input("What is your skill? ")
            skill_lvlchange = input("What is your level? ")
            data[update_name]["skills"][skills_change] = skill_lvlchange


        else:
            print("invalid")
            return
        save_contact()
        print("Updated successfully!")
    else:
        print("not found")
        print("_" * 30)
