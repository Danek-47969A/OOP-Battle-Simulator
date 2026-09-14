import random

class Hero:
    """The hero blueprint will be implemented later in the project."""
    def __init__(self, name):
        self.name = name
        self.health = 125
        self.attack_power = 20

    def attack(self):
        critical_chance = 10
        crit = random.randint(1,100)
        if crit < critical_chance:
            return random.randint(self.attack_power, 2*self.attack_power)
        else:
            return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        self.health=max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        return self.health > 0


    pass
