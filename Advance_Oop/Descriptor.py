# #
# #
# #
# # class PositiveNumber:
# #     def __set_name__(self,owner, name):
# #         self._name = name
# #     def __set__(self,instance, value):
# #         if value < 0:
# #             raise ValueError("Value must be positive")
# #         instance.__dict__[self._name] = value
# #     # noinspection PyProtectedMember
# #     def __get__(self,instance,owner):
# #         return instance.__dict__[self._name]
# # class Product:
# #     price = PositiveNumber()
# #     quantity = PositiveNumber()
# #     def __init__(self,name,price,quantity):
# #         self.name = name
# #         self.price = price
# #         self.quantity = quantity
# # product1 = Product("Milk",100,5)
# # print(product1.price)
# # print(product1.name)
# # print(product1.quantity)
# # product1.price = 655
# # product1.quantity = 10
# # print(product1.price)
# # print(product1.name)
# # print(product1.quantity)
# #
#
#
#
# class PositiveValue:
#     def __set_name__(self, owner, name):
#         self._name = name
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError("Value must be positive")
#         instance.__dict__[self._name] = value
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         else:
#          return instance.__dict__.get[self._name]
#     def __delete__(self, instance):
#         del instance.__dict__[self._name]
#         print("deleted successfully")
# class Product:
#     price = PositiveValue()
#     quantity = PositiveValue()
#     discount = PositiveValue()
#
#     def __init__(self, name, price,quantity,discount):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#         self.discount = discount
# product1 = Product("alo",100,20,10)
# print(product1.price)
# print(product1.quantity)
# print(product1.discount)
# print(Product.price)
# del product1.price
# del product1.quantity
# del product1.discount



class PositiveNumber:
    def __set_name__(self, owner, name):
        self._name = name
    def __set__(self, instance, value):
        if value < 0:
            raise AttributeError("Negative numbers are not allowed")
        else:
            instance.__dict__[self._name] = value
    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self._name)
    def __delete__(self, instance):
        del instance.__dict__[self._name]
class BankAccount:
    balance = PositiveNumber()
    withdraw_limit = PositiveNumber()
    daily_limit = PositiveNumber()

    def __init__(self,name,balance,withdraw_limit,daily_limit):
        self.name = name
        self.balance = balance
        self.withdraw_limit = withdraw_limit
        self.daily_limit = daily_limit
        self.withdrawn_today = 0
    def withdraw(self,amount):
        if amount <= 0:
            print("please enter right number")
        elif amount > self.balance:
            print("insufficient balance")
        elif amount > self.withdraw_limit:
                print("limit exceeded")
        elif self.withdrawn_today + amount > self.daily_limit:
            print("Daily limit exceeded")
        else:
            self.withdrawn_today += amount
            self.balance -= amount
            print("withdraw successful")
account1 = BankAccount("Bank Account",100,100,100)
account2 = BankAccount("Bank Account",200,100,100)
print(account1.name)
print(account2.name)
account1.withdraw(100)
print(account1.name)
print(account2.name)
account1.balance = 100
account2.balance = 200
print(account1.balance)
