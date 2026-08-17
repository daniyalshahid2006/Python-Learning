# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # class Student:
# # # # # # # # #
# # # # # # # # #     school = "FAST"
# # # # # # # # #
# # # # # # # # #     @classmethod
# # # # # # # # #     def change_school(cls, new_school):
# # # # # # # # #         cls.school = new_school
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # print(Student.school)
# # # # # # # # #
# # # # # # # # # Student.change_school("NUST")
# # # # # # # # #
# # # # # # # # # print(Student.school)
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # class Student:
# # # # # # # # #
# # # # # # # # #     count = 0
# # # # # # # # #
# # # # # # # # #     def __init__(self, name):
# # # # # # # # #         self.name = name
# # # # # # # # #         Student.count += 1
# # # # # # # # #
# # # # # # # # #     @classmethod
# # # # # # # # #     def get_count(cls):
# # # # # # # # #         print(cls.count)
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # Student("Dani")
# # # # # # # # # Student("Ali")
# # # # # # # # # Student("Ahmed")
# # # # # # # # #
# # # # # # # # # Student.get_count()
# # # # # # # # #
# # # # # # # # # class Employee:
# # # # # # # # #
# # # # # # # # #     def __init__(self, name, salary):
# # # # # # # # #         self.name = name
# # # # # # # # #         self.salary = salary
# # # # # # # # #
# # # # # # # # #     @classmethod
# # # # # # # # #     def from_string(cls, data):
# # # # # # # # #         name , salary = data.split(",")
# # # # # # # # #         return cls(name, int(salary))
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # employee = Employee.from_string("Dani,50000")
# # # # # # # # #
# # # # # # # # # print(employee.name)
# # # # # # # # # print(employee.salary)
# # # # # # # #
# # # # # # # #
# # # # # # # # class  Game:
# # # # # # # #     difficulty = "easy"
# # # # # # # #     def __init__(self,name):
# # # # # # # #         self.name = name
# # # # # # # #
# # # # # # # #     @classmethod
# # # # # # # #     def get_difficulty(cls,new_difficulty):
# # # # # # # #         cls.difficulty = new_difficulty
# # # # # # # # print(Game.difficulty)
# # # # # # # # Game.get_difficulty("medium")
# # # # # # # # print(Game.difficulty)
# # # # # # # # Game.get_difficulty("hard")
# # # # # # # # print(Game.difficulty)
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # # class Employee:
# # # # # # # #     count = 0
# # # # # # # #     def __init__(self,name,age):
# # # # # # # #         self.name = name
# # # # # # # #         self.age = age
# # # # # # # #         Employee.count += 1
# # # # # # # #     @classmethod
# # # # # # # #     def get_count(cls):
# # # # # # # #         print(cls.count)
# # # # # # # #
# # # # # # # # Employee.get_count()
# # # # # # # # employee = Employee("John",25)
# # # # # # # # employee2 = Employee("Jane",25)
# # # # # # # # Employee.get_count()
# # # # # # # # employee3 = Employee("Jne",25)
# # # # # # # # Employee.get_count()
# # # # # # # #
# # # # # # # #
# # # # # # # # class Product:
# # # # # # # #     def __init__(self,name,price):
# # # # # # # #         self.name = name
# # # # # # # #         self.price = price
# # # # # # # #     def display(self):
# # # # # # # #         print(self.name)
# # # # # # # #         print(self.price)
# # # # # # # #     @classmethod
# # # # # # # #     def from_string(cls,string):
# # # # # # # #         name,price = string.split(",")
# # # # # # # #         return cls(name,int(price))
# # # # # # # # product1 = Product.from_string("dani,1000000")
# # # # # # # # product1.display()
# # # # # # # #
# # # # # # # # class Animal:
# # # # # # # #
# # # # # # # #     species = "Animal"
# # # # # # # #
# # # # # # # #     @classmethod
# # # # # # # #     def show_species(cls):
# # # # # # # #         print(cls.species)
# # # # # # # #
# # # # # # # #
# # # # # # # # class Dog(Animal):
# # # # # # # #     species = "Dog"
# # # # # # # #
# # # # # # # #
# # # # # # # # class Cat(Animal):
# # # # # # # #     species = "Cat"
# # # # # # # #
# # # # # # # #
# # # # # # # # Animal.show_species()
# # # # # # # # Dog.show_species()
# # # # # # # # Cat.show_species()
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # # # class User:
# # # # # # # #     def __init__(self,name,age,email):
# # # # # # # #         self.name = name
# # # # # # # #         self.age = age
# # # # # # # #         self.email = email
# # # # # # # #     @classmethod
# # # # # # # #     def from_string(cls,string):
# # # # # # # #         name,age,email = string.split(',')
# # # # # # # #         return cls(name,input(age),email)
# # # # # # # #
# # # # # # # #     def display(self):
# # # # # # # #          print(self.name)
# # # # # # # #          print(self.age)
# # # # # # # #          print(self.email)
# # # # # # # # user1 = User.from_string("Daniyal,1000,suihsiuashau")
# # # # # # # # user1.display()
# # # # # # #
# # # # # # #
# # # # # # # class Vehicle:
# # # # # # #     vehicle_type = "generic"
# # # # # # #     def __init__(self,make,model,year):
# # # # # # #         self.make = make
# # # # # # #         self.model = model
# # # # # # #         self.year = year
# # # # # # #     @classmethod
# # # # # # #     def display(cls):
# # # # # # #         print(cls.vehicle_type)
# # # # # # #
# # # # # # #     @classmethod
# # # # # # #     def create(cls, make, model, year):
# # # # # # #         return cls(make, model, year)
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # # class Car(Vehicle):
# # # # # # #     vehicle_type = "car"
# # # # # # #     pass
# # # # # # # class Truck(Vehicle):
# # # # # # #     vehicle_type = "truck"
# # # # # # #     pass
# # # # # # # class Motorcycle(Vehicle):
# # # # # # #     vehicle_type = "motorcycle"
# # # # # # #     pass
# # # # # # #
# # # # # # # car1 = Car.create("bmw","mk",2000)
# # # # # # # truck1 = Truck.create("bmw","mk",2000)
# # # # # # # motorcycle1 = Motorcycle.create("bmw","mk",2000)
# # # # # # # vehicles = [car1,truck1,motorcycle1]
# # # # # # # for vehicle in vehicles:
# # # # # # #     vehicle.display()
# # # # # # #
# # # # # # class User:
# # # # # #     users = {}
# # # # # #     def __init__(self, user_id, name):
# # # # # #         self.user_id = user_id
# # # # # #         self.name = name
# # # # # #         User.users[user_id] = self
# # # # # #
# # # # # #     def display(self):
# # # # # #         print(self.user_id)
# # # # # #         print(self.name)
# # # # # #     @classmethod
# # # # # #     def find_by_id(cls, user_id):
# # # # # #         return cls.users.get(user_id)
# # # # # # user1 = User(1, "dani")
# # # # # # user2 = User(2, "name")
# # # # # # user3 = User(3, "name")
# # # # # # user1.find_by_id(1)
# # # # # # print(user1.name)
# # # # #
# # # # # # class Student:
# # # # # #     school = "Educator"
# # # # # #     def display(self):
# # # # # #         print(self.school)
# # # # # # student = Student()
# # # # # # student.display()
# # # # #
# # # # #
# # # # # class Student:
# # # # #     school = "nust"
# # # # #     def display(self):
# # # # #         print(self.school)
# # # # #     @classmethod
# # # # #     def change_name(cls,new_school):
# # # # #         cls.school = new_school
# # # # #         print(cls.school)
# # # # # student = Student()
# # # # # student.change_name("Edward")
# # # # # student.display()
# # # # from Day04_Lists.shopping_list_manager import count
# # # #
# # # #
# # # class Bank:
# # #     Bank_name = "alied"
# # #     Count = 0
# # #     def __init__(self, name, balance):
# # #         self.Name = name
# # #         self.Balance = balance
# # #         Bank.Count += 1
# # #
# # #     @classmethod
# # #     def show_count(cls):
# # #         return cls.Count
# # #     @classmethod
# # #     def change(cls,new_name):
# # #         cls.Bank_name = new_name
# # #         print(cls.Bank_name)
# # #
# # # print(Bank.show_count())
# # # bank1 = Bank("alied", 100)
# # # bank2 = Bank("alied", 200)
# # # print(bank1.show_count())
# # # print(bank2.show_count())
# # # Bank.change("alo")
# #
# #
# #
# # # class Person:
# # #     def __init__(self, name, age):
# # #         self.name = name
# # #         self.age = age
# # #     @classmethod
# # #     def from_string(cls, string):
# # #         name, age = string.split(',')
# # #         return cls(name, int(age))
# # #     def display(self):
# # #         print(self.name, self.age)
# # # Person.from_string("alo,1000")
# #
# # class User:
# #     users ={}
# #     def __init__(self,user_id, username, password):
# #         self.user_id = user_id
# #         self.username = username
# #         self.password = password
# #         User.users[user_id] = self
# #     def get_password(self):
# #         return self.password
# #     def set_password(self,password):
# #         self.password = password
# #     def display(self):
# #         print(self.user_id)
# #         print(self.username)
# #         print(self.password)
# #     @classmethod
# #     def find_by_id(cls,user_id):
# #         return cls.users.get(user_id)
# # class Use(User):
# #     def __init__(self,user_id,username,password):
# #         super().__init__(user_id,username,password)
# #     def display(self):
# #         print(self.user_id)
# #         print(self.username)
# #         print(self.get_password())
# # use1 = Use(1,"dani","123")
# # user1 = User(2,"dani","123")
# # found = use1.find_by_id(1)
# # if found:
# #     use1.display()
# #
#
#
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


