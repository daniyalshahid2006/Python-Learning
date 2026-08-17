# class Temperature:
#     @staticmethod
#     def celsius_to_fahrenheit(temp):
#         return temp * 9 / 5 + 32
# print(Temperature.celsius_to_fahrenheit(5))
# print(Temperature.celsius_to_fahrenheit(10))
#
# class Check:
#     @staticmethod
#     def is_strong(password):
#         if len(password) >= 8:
#             print('Password is strong')
#             return True
#
#         else:
#             print('Password is weak')
#             return False
# Check.is_strong("1203289121")
# print(Check.is_strong("ehfbfhedkhdbkd"))
#

class BankAccount:
    def __init__(self,owner,balance,age):
        if not self.check_age(age):
            raise ValueError("Age must be an 18 or more")
        self.owner = owner
        self.balance = balance
        self.age = age

    @staticmethod
    def check_age(age):
        return age >= 18
account1 = BankAccount("John",20000,18)
print(account1.owner)
print(account1.balance)
print(account1.age)
account2 = BankAccount("John",20000,17)
print(account2.owner)
print(account2.balance)
print(account2.age)

