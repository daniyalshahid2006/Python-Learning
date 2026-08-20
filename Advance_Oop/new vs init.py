# # # class Car:
# # #     def __new__(cls,brand,model,year,color):
# # #         print("new is running")
# # #         print("creating car")
# # #         if year < 2000:
# # #             return ("year is low")
# # #         else:
# # #          return super().__new__(cls)
# # #     def __init__(self,brand,model,year,color):
# # #         self.brand = brand
# # #         self.model = model
# # #         self.year = year
# # #         self.color = color
# # #         print("Initializing car")
# # # car = Car("Brand","Model",1000,"Blue")
# # # print(car)
# #
# #
# # class Car:
# #     def __new__(cls):
# #         print("__new__ running")
# #         return None
# #
# #     def __init__(self):
# #         print("__init__ running")
# #
# #
# # car = Car()
# #
# # print(car)
#
#
# class Database:
#     instance = None
#     initialized = False
#     def __new__(cls,name):
#         if cls.instance is None:
#             cls.instance = super().__new__(cls)
#         return cls.instance
#     def __init__(self,name):
#       if not self.initialized:
#         self.name = name
#         self.initialized = True
# db1 = Database("Bank Account")
# db2 = Database("alo")
# print(db1.name)
# print(db2.name)
# print(db1 is db2)

class PositiveNumber(int):
    def __new__(cls, value):
        if value < 0:
            raise ValueError("Negative numbers are not allowed")

        return int.__new__(cls, value)

number = PositiveNumber(100)
print(number)
print(number+ 25)
print(number- 25)
number1 = PositiveNumber(20)
print(number1)
print(number1 - 20)
print(number1 - 20)




