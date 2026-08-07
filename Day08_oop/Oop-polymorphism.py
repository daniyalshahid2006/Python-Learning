# # class Animal:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #     def sound(self):
# #         print("random sound")
# #         print(self.name)
# #         print(self.age)
# # class Dog(Animal):
# #     def __init__(self, name, age):
# #         super().__init__(name, age)
# #     def sound(self):
# #         print("dog sound")
# #         print(self.name)
# #         print(self.age)
# # class Cat(Animal):
# #     def __init__(self, name, age):
# #         super().__init__(name, age)
# #     def sound(self):
# #         print("cat sound")
# #         print(self.name)
# #         print(self.age)
# # name1 =input("enter your name")
# # age1 = int(input("enter your age"))
# # animal1 = Animal(name1, age1)
# # name2 =input("enter your name")
# # age2 = int(input("enter your age"))
# # dog = Dog(name2, age2)
# # name3 =input("enter your name")
# # age3 = int(input("enter your age"))
# # cat = Cat(name3, age3)
# # animals = [
# #     animal1,
# #     dog,
# #     cat
# # ]
# # for animal in animals:
# #     animal.sound()
#
# class Teacher:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def introduce(self):
#         print(self.name)
#         print(self.age)
#
# class Doctor:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def introduce(self):
#         print(self.name)
#         print(self.age)
#
#
# class Lawyer:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def introduce(self):
#         print(self.name)
#         print(self.age)
#
# def introduce(person):
#     person.introduce()
# name1 = input("Enter your name: ")
# age1 = input("Enter your age: ")
# teacher = Teacher(name1, age1)
# name2 = input("Enter your name: ")
# age2 = input("Enter your age: ")
# lawy = Lawyer(name2, age2)
# name3 = input("Enter your name: ")
# age3 = input("Enter your age: ")
# doctor = Doctor(name3, age3)
# introduce(teacher)
# introduce(lawy)
# introduce(doctor)


class  Cal:
    def add (self,*args):
        print(sum(args))

cal = Cal()
cal.add(1,2,3,4)