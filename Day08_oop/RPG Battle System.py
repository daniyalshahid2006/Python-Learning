from abc import ABC, abstractmethod




#pochna ha ke attack me name de sakty hn ya ni

class Character(ABC):
    def __init__(self,name,health):
        self.name = name
        self.__health = health
    def show_stats(self):
        print(f"{self.name}'s health is {self.__health}")
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
        print (f"{self.name}'s takes {amount} of damage")
        if self.__health <= 0:
            print(f"{self.name} died")
        elif self.__health <= 20:
            print(f"{self.name} is at critical health")
        else:
            pass
    @abstractmethod
    def attack(self,attacks):
        pass

class Warrior(Character):
    def __init__(self,name,health,stamina ,**kwargs):
        super().__init__(name,health)
        self.stamina = stamina
        self.info = kwargs
    def show_stats(self):
        print(f"{self.name}'s health is {self.get_health()} have stamina {self.stamina} and info is {self.info}")
    def attack(self,attacks):
        if attacks != self:
            if attacks.get_health() <= 0:
                print(f"{attacks.name} is dead cant attack")
                return
            if self.stamina >= 5:
              damage = 20
              print (f"{self.name}'s attacks a light attack of {damage}")
              attacks.damage(damage)
              self.stamina = self.stamina - 5
            else:
                print("insufficient stamina")
        else:
            print(f"Cant attack thyself")
    def special_attack(self,attacks,*bleeding):
        if attacks != self:
            if attacks.get_health() <= 0:
                print(f"{attacks.name} is dead cant attack")
                return
            if self.stamina >= 20:
                damage = 35
                print(f"{self.name}'s use a special attack on {attacks.name} ")
                if bleeding:
                    print(f"{self.name} caused bleeding on {attacks.name}")
                    damage = damage + sum (bleeding)
                attacks.damage(damage)
                self.stamina = self.stamina - 20
            else:
                print("insufficient stamina")

        else:
            print("cant attack thyself")

class Mage(Character):
    def __init__(self,name,health,mana ,**kwargs):
        super().__init__(name,health)
        self.mana = mana
        self.info = kwargs
    def show_stats(self):
        print(f"{self.name}'s health is {self.get_health()} have mana {self.mana} and info is {self.info}")
    def attack(self,attacks):
        if attacks != self:
            if attacks.get_health() <= 0:
                print(f"{attacks.name} is dead you cant attack")
                return
            if self.mana >= 10:
                damage = 25
                attacks.damage(damage)
                print(f"{self.name} attacks {attacks.name} with mana blast")
                self.mana = self.mana - 10
            else:
                print("insufficient mana")
        else:
            print("cant attack thyself")
    def fire_ball(self,attacks,*burnt):
        if attacks != self:
            if attacks.get_health() <= 0:
                print(f"{attacks.name} is dead you cant attack")
                return
            if self.mana >= 30:
                damage = 45
                print(f"{self.name} attacks {attacks.name} with a fire ball")
                if burnt:
                    print(f"{self.name} caused burnt on {attacks.name}")
                    damage = damage + sum (burnt)
                attacks.damage(damage)
                self.mana = self.mana - 30
            else:
                print("insufficient mana")
        else:
            print("cant attack thyself")
class Archer(Character):
    def __init__(self,name,health,arrows,**kwargs):
        super().__init__(name,health)
        self.arrows = arrows
        self.info = kwargs
    def show_stats(self):
        print(f"{self.name}'s health is {self.get_health()} have arrows {self.arrows} and info is {self.info}")
    def attack(self,attacks):
        if attacks != self:
            if attacks.get_health() <= 0:
                print(f"{attacks.name} is dead you cant attack")
                return
            if self.arrows >= 1:
                damage = 5
                attacks.damage(damage)
                print(f"{self.name} attacks {attacks.name} with arrows")
                self.arrows = self.arrows - 1
            else:
                print("insufficient arrows")
        else:
            print("cant attack thyself")
    def crit(self,attacks,*critical):
        if attacks != self:
            if attacks.get_health() <= 0:
                print(f"{attacks.name} is dead you cant attack")
                return
            if self.arrows >= 15:
                damage = 35
                print(f"{self.name} attacks {attacks.name} with crit")
                if critical:
                    print(f"{self.name} caused critical on {attacks.name}")
                    damage = damage + sum (critical)
                attacks.damage(damage)
                self.arrows = self.arrows - 15
            else:
                print("insufficient arrows")
        else:
            print("cant attack thyself")

name1 = input("What is your name? ")
health1 = int(input("What is your health? "))
stamina1 = int(input("What is your stamina? "))
warrior1 = Warrior(name1,health1,stamina1,muscle = 100,brain = 20)
warrior1.show_stats()
print(warrior1.get_health())

name2 = input("What is your name? ")
health2 = int(input("What is your health? "))
mana1 = int(input("What is your mana? "))
mage1 = Mage(name2,health2,mana1,muscle = 20,brain = 100)
mage1.show_stats()
print(mage1.get_health())
name3 = input("What is your name? ")
health3 = int(input("What is your health? "))
arrows1 = int(input("What is your arrows? "))
archer1 = Archer(name3,health3,arrows1,muscle = 55,brain = 50)
archer1.show_stats()
print(archer1.get_health())
warrior1.attack(warrior1)
warrior1.attack(mage1)
warrior1.special_attack(archer1,2,3,4,5)
mage1.attack(warrior1)
mage1.fire_ball(warrior1,2,2,2,2,2)
archer1.attack(warrior1)
archer1.crit(warrior1,2,3,4,5)
warrior1.show_stats()



