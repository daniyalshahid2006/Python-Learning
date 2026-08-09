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
        print(self.info)
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
        new_health = self.__health - amount
        self.set_health(new_health)
        print(f"{self.name} take {amount} of damage  ")

    def attack(self,attacks):
        print(f"{self.name} attacks  goblin ")
        attacks.damage(10)
class Warrior(Character):
    def __init__(self,name,health,stamina,**kwargs):
        super().__init__(name,health,**kwargs)
        self.stamina = stamina
    def display(self):
        print(self.name)
        print(self.get_health())
        print(self.stamina)
        print(self.info)
    def attack(self,attacks,*bleeding):
      if self.stamina > 5:
         print(f"{self.name} attacks goblin ")
         damage = 20
         if bleeding:
             damage = damage + sum(bleeding)
             print(f"{self.name} caused bleeding on goblin ")
         attacks.damage(damage)
         self.stamina = self.stamina - 5
      else:
          print("Not enough stamina")

class Mage(Character):
    def __init__(self,name,health,mana,**kwargs):
        super().__init__(name,health,**kwargs)
        self.mana = mana
    def display(self):
        print(self.name)
        print(self.mana)
        print(self.get_health())
        print(self.info)
    def attack(self,attacks,*burn):
        if self.mana > 10:
            print(f"{self.name} cast a fireball at goblin ")
            damage = 25
            if burn:
                damage = damage + sum(burn)
                print(f"{self.name} caused burning on goblin ")
            attacks.damage(damage)
            self.mana = self.mana - 10
        else:
            print("Not enough mana")

class Archer(Character):
    def __init__(self,name,health,arrows,**kwargs):
        super().__init__(name,health,**kwargs)
        self.arrows = arrows
    def display(self):
        print(self.name)
        print(self.arrows)
        print(self.get_health())
        print(self.info)

    def attack(self, attacks, *critical):
        if self.arrows > 0:
            print(f"{self.name} shoots an arrow at goblin ")
            damage = 5
            if critical:
                damage = damage + sum(critical)
                print(f"{self.name} caused critical damage on goblin ")
            attacks.damage(damage)
            self.arrows = self.arrows - 1
        else:
            print("Not enough arrows")
name1 = input("Enter your name: ")
health1 = int(input("Enter your health: "))
stamina1 = int(input("Enter your stamina: "))
warrior1 = Warrior(name1,health1,stamina1,muscle = 80,lift = 20)
warrior1.display()
print(warrior1.get_health())
goblin = Character("goblin",100,poison = 20)
goblin.display()
print(goblin.get_health())
warrior1.attack(goblin,2,3,6)
print(goblin.get_health())
warrior1.display()
name2 = input("Enter your name: ")
health2 = int(input("Enter your health: "))
mana1 = int(input("Enter your stamina: "))
Mage1 = Mage(name2,health2,mana1,poison = 20,wisdom = 80)
Mage1.display()
print(Mage1.get_health())
goblin2 = Character("goblin",100,poison = 20)
goblin2.display()
print(goblin2.get_health())
Mage1.attack(goblin2,3,3,3)
print(goblin2.get_health())
Mage1.display()
name3 = input("Enter your name: ")
health3 = int(input("Enter your health: "))
arrows1 = int(input("Enter your stamina: "))
Archer1 = Archer(name3,health3,arrows1,eyesight = 80,hearing = 20)
Archer1.display()
print(Archer1.get_health())
goblin3 = Character("goblin",100,poison = 20)
goblin3.display()
print(goblin3.get_health())
Archer1.attack(goblin3,2,2,2,2)
print(goblin3.get_health())
Archer1.display()







