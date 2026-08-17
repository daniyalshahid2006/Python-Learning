# # class Student:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #     @property
# #     def age(self):
# #         return self._age
# #     @age.setter
# #     def age(self, new_age):
# #         if new_age < 18:
# #             raise ValueError("age must be 18 or more")
# #         self._age = new_age
# #
# # student = Student("John", 18)
# # print(student.age)
# # student1 = Student("John", 10)
# # print(student1.get_age)
# # student1.get_age = 20
# # print(student1.get_age)
# #
# import math
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     @property
#     def area(self):
#         return math.pi * self.radius ** 2
#     @property
#     def radius(self):
#         return self._radius
#     @radius.setter
#     def radius(self,new_radius):
#         if new_radius < 0:
#             raise ValueError('radius cannot be negative ')
# circle = Circle(5)
# print(circle.radius)
# print(circle.area)
# circle1 = Circle(-382)
#

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value
    @property
    def state(self):
        if self.balance >= 100000:
            return "Rich"
        elif self.balance >= 50000:
            return "normal"
        else:
            return "poor"
account_1 = BankAccount("Dani", 10000)
print(account_1.name)
print(account_1.balance)
print(account_1.state)
account_2 = BankAccount("Dani", -50000)
print(account_2.name)
print(account_2.balance)
print(account_2.state)