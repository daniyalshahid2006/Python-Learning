# # # # # class Animal:
# # # # #     def __init__(self, name, age):
# # # # #         self.name = name
# # # # #         self.age = age
# # # # #     def sound(self):
# # # # #         print("random sound")
# # # # #         print(self.name)
# # # # #         print(self.age)
# # # # # class Dog(Animal):
# # # # #     def __init__(self, name, age):
# # # # #         super().__init__(name, age)
# # # # #     def sound(self):
# # # # #         print("dog sound")
# # # # #         print(self.name)
# # # # #         print(self.age)
# # # # # class Cat(Animal):
# # # # #     def __init__(self, name, age):
# # # # #         super().__init__(name, age)
# # # # #     def sound(self):
# # # # #         print("cat sound")
# # # # #         print(self.name)
# # # # #         print(self.age)
# # # # # name1 =input("enter your name")
# # # # # age1 = int(input("enter your age"))
# # # # # animal1 = Animal(name1, age1)
# # # # # name2 =input("enter your name")
# # # # # age2 = int(input("enter your age"))
# # # # # dog = Dog(name2, age2)
# # # # # name3 =input("enter your name")
# # # # # age3 = int(input("enter your age"))
# # # # # cat = Cat(name3, age3)
# # # # # animals = [
# # # # #     animal1,
# # # # #     dog,
# # # # #     cat
# # # # # ]
# # # # # for animal in animals:
# # # # #     animal.sound()
# # # #
# # # # class Teacher:
# # # #     def __init__(self, name, age):
# # # #         self.name = name
# # # #         self.age = age
# # # #
# # # #     def introduce(self):
# # # #         print(self.name)
# # # #         print(self.age)
# # # #
# # # # class Doctor:
# # # #     def __init__(self, name, age):
# # # #         self.name = name
# # # #         self.age = age
# # # #
# # # #     def introduce(self):
# # # #         print(self.name)
# # # #         print(self.age)
# # # #
# # # #
# # # # class Lawyer:
# # # #     def __init__(self, name, age):
# # # #         self.name = name
# # # #         self.age = age
# # # #
# # # #     def introduce(self):
# # # #         print(self.name)
# # # #         print(self.age)
# # # #
# # # # def introduce(person):
# # # #     person.introduce()
# # # # name1 = input("Enter your name: ")
# # # # age1 = input("Enter your age: ")
# # # # teacher = Teacher(name1, age1)
# # # # name2 = input("Enter your name: ")
# # # # age2 = input("Enter your age: ")
# # # # lawy = Lawyer(name2, age2)
# # # # name3 = input("Enter your name: ")
# # # # age3 = input("Enter your age: ")
# # # # doctor = Doctor(name3, age3)
# # # # introduce(teacher)
# # # # introduce(lawy)
# # # # introduce(doctor)
# # #
# # #
# # # class  Cal:
# # #     def add (self,*args):
# # #         print(sum(args))
# # #
# # # cal = Cal()
# # # cal.add(1,2,3,4)
# #
# #
# #
# # class Calculator:
# #     def calculate(self,*args,**kwargs):
# #         print(sum(args)+sum(kwargs.values()))
# #         print(sum(args))
# #         print(sum(kwargs.values()))
# # cal1 = Calculator()
# # cal2 = Calculator()
# # cal3 = Calculator()
# #
# # cal1.calculate(1,2)
# # cal2.calculate(first = 10, second = 20)
# # cal3.calculate(1,2,third= 30, fourth= 40)
# from tokenize import group
#
#
# class Character:
#     def __init__(self,name,health):
#         self.name = name
#         self.health = health
#     def attack(self):
#         print(f"{self.name} Attacks")
# class Warrior(Character):
#     def __init__(self,name,health):
#         super().__init__(name,health)
#     def attack(self):
#         print(f"{self.name} Attacks with a sword")
# class Mage(Character):
#     def __init__(self,name,health):
#         super().__init__(name,health)
#     def attack(self):
#         print(f"{self.name} cast a fireball")
# class Archer(Character):
#     def __init__(self,name,health):
#         super().__init__(name,health)
#     def attack(self):
#         print(f"{self.name} shoots an arrow")
# name1 = input("What is your name?")
# health1 = int(input("What is your health?"))
# warrior1 = Warrior(name1,health1)
# name2 = input("What is your name?")
# health2 = int(input("What is your health?"))
# mage1 = Mage(name2,health2)
# name3 = input("What is your name?")
# health3 = int(input("What is your health?"))
# archer1 = Archer(name3,health3)
#
# Group = [
#     warrior1,
#     mage1,
#     archer1
# ]
# for Group in Group:
#     Group.attack()