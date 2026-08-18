#
#
#
# class PositiveNumber:
#     def __set_name__(self,owner, name):
#         self._name = name
#     def __set__(self,instance, value):
#         if value < 0:
#             raise ValueError("Value must be positive")
#         instance.__dict__[self._name] = value
#     # noinspection PyProtectedMember
#     def __get__(self,instance,owner):
#         return instance.__dict__[self._name]
# class Product:
#     price = PositiveNumber()
#     quantity = PositiveNumber()
#     def __init__(self,name,price,quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
# product1 = Product("Milk",100,5)
# print(product1.price)
# print(product1.name)
# print(product1.quantity)
# product1.price = 655
# product1.quantity = 10
# print(product1.price)
# print(product1.name)
# print(product1.quantity)
#
from itertools import product


class PositiveValue:
    def __set_name__(self, owner, name):
        self._name = name
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value must be positive")
        instance.__dict__[self._name] = value
    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
         return instance.__dict__[self._name]
class Product:
    price = PositiveValue()
    quantity = PositiveValue()
    discount = PositiveValue()

    def __init__(self, name, price,quantity,discount):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.discount = discount
product1 = Product("alo",100,20,10)
print(product1.price)
print(product1.quantity)
print(product1.discount)
print(Product.price)



