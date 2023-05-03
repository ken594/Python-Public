import random
from game_classes.fighter import Fighter

class Ninja(Fighter):
    def __init__(self):
        super().__init__()
        self.name = "Ninja"
        self.buff = "Pow"
        self.special = "Sweeping leg kick"
        self.strength = 8
        self.agility = 8

    def attack(self, target):
        print(f'{self.name} is attacking {target.name}')
        target.defend(int(self.strength*0.5 + self.agility*0.5))

    def use_special(self, target):
        # 50% stun and attack target
        print(f"{self.name} uses {self.special}")
        chance = random.randint(1,2)
        if chance == 1:
            print(f"Stun and attack the {target.name} by its agility!")
            target.defend(self.agility)
            target.stun = 1
        else:
            print(f"Unlucky, maybe next time!")

    def use_buff(self):
        print(f'{self.name} uses {self.buff}')
        self.health += int(self.agility*0.5)
        if self.health > 100:
            self.health = 100
        self.agility += 3
        print(f"Its health is up by {self.agility} and agility is up by 3, it is now health: {self.health}, agility: {self.agility}")

#  class Ninja(Fighter):
#     def __init__(self):
#         super().__init__()
#         self.name = "John Wayne"
#         self.buff = "YeeHaww"
#         self.special = "Six shooter attack"

#     def use_special(self,target):
#         chance = random.randint(1,2)
#         if chance > 1:
#             print(f'Lucky hit! {self.name} fires twice')
#             target.defend(10)
#             target.defend(10)
#         else:
#             print(f'{self.name} fires once')
#             target.defend(10)

#     def use_buff(self):
#         print(f'{self.name} screams YEEEHAWWW!')
#         self.strength += 3
#         print(f'{self.name} is fired up, strength up by 3, it is now {self.strength}')