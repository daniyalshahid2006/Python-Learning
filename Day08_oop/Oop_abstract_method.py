# from abc import ABC, abstractmethod
# class Character(ABC):
#     def __init__(self,name,health):
#         self.name = name
#         self.__health = health
#     def display(self):
#         print(f"{self.name} have {self.__health} health")
#     def get_health(self):
#         return self.__health
#     def set_health(self,new_health):
#         if new_health > 100:
#             self.__health = 100
#         elif new_health < 0:
#             self.__health = 0
#         else:
#             self.__health = new_health
#     def damage(self,amount):
#         new_health = self.__health - amount
#         self.set_health(new_health)
#         print(f"{self.name} takes {amount} amount of damage")
#     @abstractmethod
#     def attack(self,attacks):
#         pass
# class Warrior(Character):
#     def __init__(self,name,health,stamina):
#         super().__init__(name,health)
#         self.stamina = stamina
#     def display(self):
#         print(f"{self.name} have {self.get_health()} health and {self.stamina} stamina")
#     def attack(self,attacks,*bleeding):
#         if self.stamina >= 5:
#             print(f"{self.name} attacks with a sword")
#             damage = 20
#             if bleeding:
#                 damage = damage + sum(bleeding)
#                 print(f"{self.name} caused bleeding ")
#             attacks.damage(damage)
#             self.stamina = self.stamina - 5
#         else:
#             print(f"{self.name} have insufficient stamina")
# class Mage(Character):
#     def __init__(self,name,health,mana):
#         super().__init__(name,health)
#         self.mana = mana
#     def display(self):
#         print(f"{self.name} have {self.get_health()} health and {self.mana} mana")
#     def attack(self,attacks,*burn):
#         if self.mana >= 10:
#             print(f"{self.name} cast a fireball")
#             damage = 25
#             if burn:
#                 damage = damage + sum(burn)
#                 print(f"{self.name} caused burn")
#             attacks.damage(damage)
#             self.mana = self.mana - 10
#         else:
#             print(f"{self.name} have insufficient mana")
# class Goblin(Character):
#     def __init__(self,name,health,**kwargs):
#         super().__init__(name,health)
#         self.info = kwargs
#     def display(self):
#         print(f"{self.name} have {self.get_health()} health and {self.info}")
#     def attack(self,attacks):
#         pass
# name1 = input("What is your name?")
# health1 = int(input("What is your health?"))
# strength1 = int(input("What is your strength?"))
# Warrior1 = Warrior(name1,health1,strength1)
# Warrior1.display()
# print(Warrior1.get_health())
# name2 = input("What is your name?")
# health2 = int(input("What is your health?"))
# goblin1 = Goblin(name2,health2,poison = 23)
# goblin1.display()
# print(goblin1.get_health())
# Warrior1.attack(goblin1,2,3,4)
# Warrior1.display()
# print(goblin1.get_health())
# name3 = input("What is your name?")
# health3 = int(input("What is your health?"))
# mana1 = int(input("What is your mana?"))
# Mage1 = Mage(name3,health3,mana1)
# Mage1.display()
# print(Mage1.get_health())
# Mage1.attack(goblin1,2,3,4)
# Mage1.display()
# print(goblin1.get_health())
# Mage1.attack(Mage1,2,3,4)
# Mage1.display()
#
import random
from abc import ABC, abstractmethod
class Character(ABC):
    def __init__(self, name,health):
        self.name = name
        self.__health = health
    def display(self):
        print(self.name)
        print(self.__health)
    def get_health(self):
        return self.__health
    def set_health(self,new_health):
        if new_health > 100:
            self.__health = 100
        elif new_health < 0:
            self.__health = 0
        else:
            self.__health = new_health
    def damage(self,amount):
        new_health = self.__health - amount
        self.set_health(new_health)
        print(f"{self.name} takes {amount} of damage")
    @abstractmethod
    def attack(self,attacks):
        pass
class Warrior(Character):
    def __init__(self,name,health,stamina):
        super().__init__(name,health)
        self.stamina = stamina
    def display(self):
        print(self.name)
        print(self.get_health())
        print(self.stamina)
    def attack(self,attacks):
      if attacks != self:
        if self.stamina >= 5:
            print(f"{self.name} do a basic attacks {attacks} with a sword ")
            damage = 20
            attacks.damage(damage)
            self.stamina = self.stamina- 5
        else:
            print(f"{self.name} have insufficient stamina")
      else:
          print(f"cant attack thyself")
    def heavy_attack(self,attacks):
      if attacks != self:
        if self.stamina >= 20:
            print(f"{self.name} do a heavy attacks {attacks} with a sword ")
            damage = 40
            attacks.damage(damage)
            self.stamina = self.stamina- 20
        else:
            print(f"{self.name} have insufficient stamina")
      else:
          print(f"cant attack thyself")
class Mage(Character):
    def __init__(self,name,health,mana):
        super().__init__(name,health)
        self.mana = mana
    def display(self):
        print(self.name)
        print(self.get_health())
        print(self.mana)
    def attack(self,attacks):
      if attacks != self:
        if self.mana >= 10:
            print(f"{self.name} cast a magic attack {attacks}")
            damage = 25
            attacks.damage(damage)
            self.mana = self.mana - 5
        else:
            print(f"{self.name} have insufficient mana")
      else:
            print(f"cant attack thyself")
    def fire_ball(self,attacks,burnt):
      if attacks != self:
        if self.mana >= 30:
            print(f"{self.name} cast a fire ball")
            damage = 50
            if random.random() < 0.4:
                damage =  damage + 10
                print(f"{self.name} cast burnt")
            attacks.damage(damage)
            self.mana = self.mana - 30
        else:
            print(f"{self.name} have insufficient mana")
      else:
          print(f"cant attack thyself")

class Goblin(Character):
    def __init__(self,name,health,poison):
        super().__init__(name,health)
        self.poison = poison
    def display(self):
        print(self.name)
        print(self.get_health())
        print(self.poison)
    def attack(self,attacks):
        if attacks != self:
            if self.poison >= 5:
                print(f"{self.name} attack with poison {attacks}")
                damage = 20
                if random.random() < 0.4:
                    damage = damage + 2+2+2+2+2
                    print(f"{self.name} cast poison")
                attacks.damage(damage)
                self.poison = self.poison - 5
            else:
                print(f"{self.name} have insufficient poison")
        else:
            print(f"cant attack thyself")

name1 = input("What is your name?")
health1 = int(input("What is your health?"))
stamina1 = int(input("What is your stamina?"))
Warrior1 = Warrior(name1,health1,stamina1)
Warrior1.display()
print(Warrior1.get_health())
Warrior1.attack(Warrior1)
print(Warrior1.get_health())
goblin1 = Goblin(name1,health1,stamina1)
goblin1.display()
print(goblin1.get_health())
Warrior1.attack(goblin1)
print(goblin1.get_health())
mage1 = Mage(name1,health1,stamina1)
mage1.display()
print(mage1.get_health())
mage1.attack(mage1)
print(mage1.get_health())



