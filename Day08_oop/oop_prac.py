# # # class car:
# # #     def __init__(self, brand, model, year):
# # #         self.make = brand
# # #         self.model = model
# # #         self.year = year
# # #
# # #     def describe(self):
# # #         print(f"{self.make} {self.model} {self.year}")
# # #
# # #
# # # car1 = car("BMW", "M3gtr", 2001)
# # # car1.describe()
# # # car2 = car("supra","m3",20001)
# # # car2.describe()
# #
# # class Bank_Account:
# #     def __init__(self,name,balance):
# #         self.name = name
# #         self.balance = balance
# #
# #     def deposit(self,amount):
# #         if amount > 0:
# #             self.balance += amount
# #     def withdraw(self,amount):
# #         if amount > 0 and amount <= self.balance:
# #             self.balance -= amount
# #     def check_balance(self):
# #         print(f"{self.name}'s balance is {self.balance}")
# #
# # account1 = Bank_Account("John",500)
# # account1.deposit(10)
# # account1.withdraw(5)
# # account1.check_balance()
# class player:
#     def __init__(self,name,health):
#         self.name=name
#         self.health=health
#     def take_damage(self,damage):
#         if damage<=self.health:
#             self.health-=damage
#         else:
#             self.health=0
#     def heal(self,amount):
#         if amount + self.health <= 100:
#             self.health+=amount
#         else:
#             self.health = 100
#     def show_health(self):
#         print(f"{self.name} health is: {self.health}")
# name=input("Enter your name:")
# player1=player(name,100)
# damage = int(input("Enter your damage:"))
# player1.take_damage(damage)
# player1.show_health()
# amount=int(input("Enter your amount:"))
# player1.heal(amount)
# player1.show_health()
class Laptop:
    def __init__(self, brand, ram ,storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage
    def upgrade_ram(self,extra_ram):
        self.ram += extra_ram
        print("ram upgraded")
    def downgrade_ram(self,reducing_ram):
        self.ram -= reducing_ram
        print("ram downgraded")
    def upgrade_storage(self,extra_storage):
        self.storage += extra_storage
        print("storage upgraded")
    def downgrade_storage(self,reducing_storage):
        self.storage -= reducing_storage
        print("storage downgraded")
    def showspecs(self):
        print(f"brand: {self.brand}, ram: {self.ram}, storage: {self.storage}")
brand = input("enter brand: ")
ram = int(input("enter ram: "))
storage = int(input("enter storage: "))
laptop = Laptop(brand,ram,storage)
laptop.showspecs()
extra_ram = int(input("enter extra ram: "))
laptop.upgrade_ram(extra_ram)
laptop.showspecs()
reducing_ram = int(input("enter reducing ram: "))
laptop.downgrade_ram(reducing_ram)
laptop.showspecs()
extra_storage = int(input("enter extra storage: "))
laptop.upgrade_storage(extra_storage)
laptop.showspecs()
reducing_storage = int(input("enter reducing storage: "))
laptop.downgrade_storage(reducing_storage)
laptop.showspecs()
