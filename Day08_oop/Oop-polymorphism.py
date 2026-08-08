# # # # # # class Animal:
# # # # # #     def __init__(self, name, age):
# # # # # #         self.name = name
# # # # # #         self.age = age
# # # # # #     def sound(self):
# # # # # #         print("random sound")
# # # # # #         print(self.name)
# # # # # #         print(self.age)
# # # # # # class Dog(Animal):
# # # # # #     def __init__(self, name, age):
# # # # # #         super().__init__(name, age)
# # # # # #     def sound(self):
# # # # # #         print("dog sound")
# # # # # #         print(self.name)
# # # # # #         print(self.age)
# # # # # # class Cat(Animal):
# # # # # #     def __init__(self, name, age):
# # # # # #         super().__init__(name, age)
# # # # # #     def sound(self):
# # # # # #         print("cat sound")
# # # # # #         print(self.name)
# # # # # #         print(self.age)
# # # # # # name1 =input("enter your name")
# # # # # # age1 = int(input("enter your age"))
# # # # # # animal1 = Animal(name1, age1)
# # # # # # name2 =input("enter your name")
# # # # # # age2 = int(input("enter your age"))
# # # # # # dog = Dog(name2, age2)
# # # # # # name3 =input("enter your name")
# # # # # # age3 = int(input("enter your age"))
# # # # # # cat = Cat(name3, age3)
# # # # # # animals = [
# # # # # #     animal1,
# # # # # #     dog,
# # # # # #     cat
# # # # # # ]
# # # # # # for animal in animals:
# # # # # #     animal.sound()
# # # # #
# # # # # class Teacher:
# # # # #     def __init__(self, name, age):
# # # # #         self.name = name
# # # # #         self.age = age
# # # # #
# # # # #     def introduce(self):
# # # # #         print(self.name)
# # # # #         print(self.age)
# # # # #
# # # # # class Doctor:
# # # # #     def __init__(self, name, age):
# # # # #         self.name = name
# # # # #         self.age = age
# # # # #
# # # # #     def introduce(self):
# # # # #         print(self.name)
# # # # #         print(self.age)
# # # # #
# # # # #
# # # # # class Lawyer:
# # # # #     def __init__(self, name, age):
# # # # #         self.name = name
# # # # #         self.age = age
# # # # #
# # # # #     def introduce(self):
# # # # #         print(self.name)
# # # # #         print(self.age)
# # # # #
# # # # # def introduce(person):
# # # # #     person.introduce()
# # # # # name1 = input("Enter your name: ")
# # # # # age1 = input("Enter your age: ")
# # # # # teacher = Teacher(name1, age1)
# # # # # name2 = input("Enter your name: ")
# # # # # age2 = input("Enter your age: ")
# # # # # lawy = Lawyer(name2, age2)
# # # # # name3 = input("Enter your name: ")
# # # # # age3 = input("Enter your age: ")
# # # # # doctor = Doctor(name3, age3)
# # # # # introduce(teacher)
# # # # # introduce(lawy)
# # # # # introduce(doctor)
# # # #
# # # #
# # # # class  Cal:
# # # #     def add (self,*args):
# # # #         print(sum(args))
# # # #
# # # # cal = Cal()
# # # # cal.add(1,2,3,4)
# # #
# # #
# # #
# # # class Calculator:
# # #     def calculate(self,*args,**kwargs):
# # #         print(sum(args)+sum(kwargs.values()))
# # #         print(sum(args))
# # #         print(sum(kwargs.values()))
# # # cal1 = Calculator()
# # # cal2 = Calculator()
# # # cal3 = Calculator()
# # #
# # # cal1.calculate(1,2)
# # # cal2.calculate(first = 10, second = 20)
# # # cal3.calculate(1,2,third= 30, fourth= 40)
# # from tokenize import group
# #
# #
# # class Character:
# #     def __init__(self,name,health):
# #         self.name = name
# #         self.health = health
# #     def attack(self):
# #         print(f"{self.name} Attacks")
# # class Warrior(Character):
# #     def __init__(self,name,health):
# #         super().__init__(name,health)
# #     def attack(self):
# #         print(f"{self.name} Attacks with a sword")
# # class Mage(Character):
# #     def __init__(self,name,health):
# #         super().__init__(name,health)
# #     def attack(self):
# #         print(f"{self.name} cast a fireball")
# # class Archer(Character):
# #     def __init__(self,name,health):
# #         super().__init__(name,health)
# #     def attack(self):
# #         print(f"{self.name} shoots an arrow")
# # name1 = input("What is your name?")
# # health1 = int(input("What is your health?"))
# # warrior1 = Warrior(name1,health1)
# # name2 = input("What is your name?")
# # health2 = int(input("What is your health?"))
# # mage1 = Mage(name2,health2)
# # name3 = input("What is your name?")
# # health3 = int(input("What is your health?"))
# # archer1 = Archer(name3,health3)
# #
# # Group = [
# #     warrior1,
# #     mage1,
# #     archer1
# # ]
# # for Group in Group:
# #     Group.attack()
#
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def move(self):
#         print(self.make, self.model, self.year)
#         print("car goo vroom vroom")
# class Boat:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def move(self):
#         print(self.make, self.model, self.year)
#         print("boat goo pshhhhh")
#
# class Airplane:
#      def __init__(self, make, model, year):
#          self.make = make
#          self.model = model
#          self.year = year
#      def move(self):
#         print(self.make, self.model, self.year)
#         print("airplane goo neooooo")
#
# def move(vehicle):
#     vehicle.move()
#
#
# make1 = input("Enter your make: ")
# model1 = input("Enter your model: ")
# year1 = int(input("Enter your year: "))
# car1 = Car(make1, model1, year1)
# make2 = input("Enter your make: ")
# model2 = input("Enter your model: ")
# year2 = int(input("Enter your year: "))
# boat1 = Boat(make2, model2, year2)
# make3 = input("Enter your make: ")
# model3 = input("Enter your model: ")
# year3 = int(input("Enter your year: "))
# airplane1 = Airplane(make3, model3, year3)
# move(car1)
# move(boat1)
# move(airplane1)




class Character:
    def __init__(self, name,health,**kwargs):
        self.name = name
        self.__health = health
        self.info = kwargs
    def display(self):
        print(self.name)
        print(self.__health)
    def get_health(self):
        return self.__health
    def set_health(self,new_health):
        if new_health >100:
            self.__health = 100
        elif new_health < 0:
            self.__health = 0
        else:
            self.__health = new_health
    def damage(self,amount):
        print(f"goblin take{amount} of damage ")
    def attack(self,attacks):
        print(f"{self.name} attacks {attacks} goblin ")
        attacks.damage(10)
    def goblin_health(self,health):
        

class Warrior(Character):
    def __init__(self,name,health,mana,**kwargs):
        super().__init__(name,health,**kwargs)
        self.mana = mana
    def display(self):
        print(self.name)
        print(self.get_health())
        print(self.mana)
    def attack(self,attacks,*bleeding):
        print(f"{self.name} attacks {attacks} goblin ")
        attacks.damage(20)










