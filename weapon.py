from ability import ability
import random

class weapon(ability):
    def attack(self):
        half = int(self.max_damage/2)
        return random.randint(half, self.max_damage)    
