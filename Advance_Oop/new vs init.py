# # # # class Car:
# # # #     def __new__(cls,brand,model,year,color):
# # # #         print("new is running")
# # # #         print("creating car")
# # # #         if year < 2000:
# # # #             return ("year is low")
# # # #         else:
# # # #          return super().__new__(cls)
# # # #     def __init__(self,brand,model,year,color):
# # # #         self.brand = brand
# # # #         self.model = model
# # # #         self.year = year
# # # #         self.color = color
# # # #         print("Initializing car")
# # # # car = Car("Brand","Model",1000,"Blue")
# # # # print(car)
# # #
# # #
# # # class Car:
# # #     def __new__(cls):
# # #         print("__new__ running")
# # #         return None
# # #
# # #     def __init__(self):
# # #         print("__init__ running")
# # #
# # #
# # # car = Car()
# # #
# # # print(car)
# #
# #
# # class Database:
# #     instance = None
# #     initialized = False
# #     def __new__(cls,name):
# #         if cls.instance is None:
# #             cls.instance = super().__new__(cls)
# #         return cls.instance
# #     def __init__(self,name):
# #       if not self.initialized:
# #         self.name = name
# #         self.initialized = True
# # db1 = Database("Bank Account")
# # db2 = Database("alo")
# # print(db1.name)
# # print(db2.name)
# # print(db1 is db2)
#
# # class PositiveNumber(int):
# #     def __new__(cls, value):
# #         if value < 0:
# #             raise ValueError("Negative numbers are not allowed")
# #
# #         return int.__new__(cls, value)
# #
# # number = PositiveNumber(100)
# # print(number)
# # print(number+ 25)
# # print(number- 25)
# # number1 = PositiveNumber(20)
# # print(number1)
# # print(number1 - 20)
# # print(number1 - 20)
#
#
# # class Number:
# #     catch = {}
# #     def __new__(cls,value):
# #         key = (cls,value)
# #         if key in cls.catch:
# #             return cls.catch[key]
# #         obj = super().__new__(cls)
# #         cls.catch[key] = obj
# #         return obj
# #     def __init__(self,value):
# #         self.value = value
# # a = Number("a")
# # b = Number("b")
# # c = Number("a")
# # print(a.value)
# # print(a is b)
# # print(a is c)
#
#
# # import copy
# # class namo:
# #     def __init__(self,name):
# #         self.name = name
# # a = namo("Alo")
# # b = copy.deepcopy(a)
# # print(a)
# # print(b)
# # print(a is b)
#
#
# import pickle
# class BankAccount:
#     def __init__(self,name,balance,deposit,withdraw):
#         self.name = name
#         self.balance = balance
#         self.deposit = deposit
#         self.withdraw = withdraw
# person1 = BankAccount("Bank Account",100,5,100)
# person2 = pickle.dumps(person1)
# print(person2)
# data = pickle.dumps(person1)
# person3 = pickle.loads(data)
# print(person3)
# print(person1 is person3)



class BankAccount:
    check = {}
    def __new__(cls,account_number,name,balance):
        key = (cls,account_number)
        if key in cls.check:
            return cls.check[key]
        if balance < 0:
            raise ValueError("Negative Balance")
        else:
         obj = object.__new__(cls)
         cls.check[key] = obj
         return obj
    def __init__(self,account_number,name,balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
account1 = BankAccount(100,"dani",100)
account2 = BankAccount(100,"daio",100)
print(account1 is account2)
account3 = BankAccount(1100,"dani",100)
print(account3 is account2)




