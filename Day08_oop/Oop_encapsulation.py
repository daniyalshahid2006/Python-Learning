# # # class student:
# # #     def __init__(self, name,number, marks):
# # #         self.name = name
# # #         self._number = number
# # #         self.__marks = marks
# # #     def show_stats(self):
# # #         print(self.name)
# # #         print(self._number)
# # #     def get_marks(self):
# # #         print(self.__marks)
# # # student1=student("Dani", "33839298382" ,70)
# # # student1.show_stats()
# # # student1.get_marks()
# #
# # class Employee:
# #     def __init__(self,name,salary):
# #         self.name = name
# #         self.__salary = salary
# #     def show_stats(self):
# #         print(f"name: {self.name}\nself.salary: {self.__salary}")
# #     def get_salary(self):
# #         print(self.__salary)
# #     def set_salary(self,new_salary):
# #         if new_salary > 0:
# #             self.__salary = new_salary
# #             print("salary updated successfully")
# #         else:
# #             print("salary updated failed")
# # name =input("enter your name: ")
# # emp = Employee(name,100000)
# # emp.show_stats()
# # emp.get_salary()
# # emp.set_salary(200000)
# # emp.show_stats()
#
# class Phone:
#     def __init__(self,brand,battery):
#         self.brand = brand
#         self.__battery = battery
#     def show_stats(self):
#         print(f"brand: {self.brand} \n battery: {self.__battery}")
#     def get_battery(self):
#         return self.__battery
#     def charge(self,amount):
#         self.__battery += amount
#
#         if self.__battery > 100:
#             self.__battery = 100
#     def use (self,amount):
#         self.__battery -= amount
#
#         if self.__battery < 0:
#             self.__battery = 0
#             print("phone died")
# brand1 = input("enter brand: ")
# battery1 = int(input("enter battery: "))
# phone1 = Phone(brand1,battery1)
# phone1.show_stats()
# amount1 = int(input("enter charging amount: "))
# phone1.charge(amount1)
# phone1.show_stats()
# use = int(input("enter usage amount: "))
# phone1.use (use)
# phone1.show_stats()
# print(phone1.get_battery())


class Character:
    def __init__(self,name,health):
        self.name = name
        self.__health = health
    def show_stats(self):
        print(f"{self.name} health is: {self.__health}")
    def get_health(self):
        return self.__health
    def set_health(self,value):
        if value < 0:
            self.__health = 0
        elif value > 100:
            self.__health = 100
        else:
            self.__health = value
    def take_damage(self,damage):
        self.set_health(self.get_health()-damage)
class Mage(Character):
    def __init__(self,name,health,mana):
        super().__init__(name,health)
        self.__mana = mana
    def show_stats(self):
        print(f"name: {self.name} \nHealth: {self.get_health()} \nmana: {self.__mana}")
    def get_mana(self):
        return self.__mana
    def set_mana(self,value):
        if value < 0:
            self.__mana = 0
        elif value > 100:
            self.__mana = 100
        else:
            self.__mana = value
    def cast_spell(self,spell):
        current =self.get_mana()
        if spell <= current:
            new = current - spell
            self.set_mana(new)
            print(f"{self.name} Cast fire ball")
        else:
            print(f"{self.name} have insufficient mana")
name1 = input("What is your name? ")
health1 = int(input("What is your health? "))
mana1 = int(input("What is your mana? "))
character1 = Mage(name1,health1,mana1)
character1.show_stats()
amount1 = int(input("what is your current health? "))
character1.set_health(amount1)
character1.show_stats()
print(character1.get_health())
character1.take_damage(30)
print(character1.get_health())
character1.take_damage(20)
print(character1.get_health())
amount2 = int(input("whats your current mana? "))
character1.set_mana(amount2)
character1.show_stats()
print(character1.get_mana())
spell1=int(input("What is your spell cost?"))
character1.cast_spell(spell1)
print(character1.get_mana())






