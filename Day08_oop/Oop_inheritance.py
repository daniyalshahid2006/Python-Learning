#
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(f"{self.name} is {self.age} years old")
# class Student(Person):
#     def __init__(self,name,age,grade):
#         super().__init__(name,age)
#         self.grade = grade
# def displayy(self):
#     print(f"{self.name} is {self.age} years old his grade is {self.grade}")
# name = input("Enter your name:")
# age = input("Enter your age:")
# grade = input("Enter your grade:")
# student1 = Student(name,age,grade)
# name = input("Enter your name:")
# age = input("Enter your age:")
# grade = input("Enter your grade:")
# student2 = Student(name,age,grade)
# student1.display()
# student2.display()

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, attacks):
        print(f"{self.name} attacks {attacks} ")

    def show_stats(self):
        print(f"{self.name} has {self.health} health")


class Mage(Character):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana

    def show_stats(self):
        print(f"Name:{self.name}\nHealth:{self.health}\nMana:{self.mana}")

    def cast_spell(self, spell_cost):
        if self.mana >= spell_cost:
            self.mana -= spell_cost
            print(f"{self.name} casts fire ball")

        else:
         print("mana is too low")


name = input("What is your name? ")
health = int(input("What is your health? "))
mana = int(input("What is your mana? "))
mage1 = Mage(name, health, mana)
mage1.show_stats()
mage1.attack("goblin")
mage1.show_stats()
mage1.cast_spell(20)
mage1.cast_spell(30)
mage1.cast_spell(20)
mage1.cast_spell(25)
mage1.cast_spell(20)
mage1.show_stats()

