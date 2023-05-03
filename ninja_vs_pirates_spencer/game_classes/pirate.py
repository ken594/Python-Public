import random
from game_classes.fighter import Fighter

class Pirate(Fighter):
    def __init__(self):
        super().__init__()
        self.name = "Pirate"
        self.buff = "Gun Upgrade"
        self.special = "Fire in the Hole"
        self.agility = 3
        self.defense = 5

    def attack(self, target):
        return super().attack(target)

    def use_buff(self):
        print(f'{self.name} uses {self.buff}')
        self.strength += 3
        self.defense += 1
        print(f"Its strength is up by 3 and defense is up by 3, it is now strength: {self.strength}, defense: {self.defense}")

    def use_special(self, target):
        # 50% to do 150% dmg
        print(f"{self.name} uses {self.special}")
        chance = random.randint(1,2)
        if chance == 1:
            print(f"Normal attack")
            target.defend(self.strength)
        else:
            print(f"Critical Attack!")
            target.defend(int(self.strength * 1.5))

# class Pirate(Fighter):
#     def __init__(self):
#         super().__init__()
#         self.name = "Van Damme"
#         self.agility += 8
#         self.special = "The Splits"
#         self.buff = "Defensive Stance"

#     def use_special(self, target):
#         target.defend(self.agility)
#         print(f"{self.name} does the splits and it's amazing!")

#     def use_buff(self):
#         self.defense += 2
#         print(f'{self.name} uses {self.buff} ')
#         print(f'Defense raised to {self.defense}')

