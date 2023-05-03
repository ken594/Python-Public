class Fighter:
    def __init__(self):
        self.name = "Default Character Name"
        self.health = 100
        self.strength = 10
        self.agility = 5
        self.defense = 3
        self.special = "not implemented"
        self.buff = "not implemented"
        self.stun = 0


    def attack(self, target):
        print(f'{self.name} is attacking {target.name}')
        target.defend(int(self.strength))

    def defend(self, amount):
        damage = amount - self.defense
        if damage < 0:
            damage = 0
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f'{self.name} took {damage} and now has {self.health} health')

    def use_special(self):
        raise NotImplementedError
    
    def use_buff(self):
        raise NotImplementedError
    
# print('fighter module loaded')