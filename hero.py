import random
class hero:

    def __init__(self, name, starting_health=100):
        self._name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)
    
    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_armor(self, armor):
        self.armors.append(armor)
    
    def add_kill(self, num):
        self.kills += num
    
    def add_death(self, num):
        self.kills += num

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self, damage):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        damage -= total_block
        return damage

    def take_damage(self, damage):
        x = self.defend(damage)
        self.current_health -= x
        
    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        opponent.take_damage(self.attack())
        self.take_damage(opponent.attack())
        print(0)
        if opponent.is_alive() == False and self.is_alive() == True:
            self.add_kill(1)
            opponent.add_death(1)
            print(1)
            return 1
        elif self.is_alive() == False and opponent.is_alive() == True:
            self.add_death(1)
            opponent.add_kill(1)
            print(2)
            return 2
        elif self.is_alive() == False and opponent.is_alive() == False:
            print("DOUBLE KILL")
            self.add_kill(1)
            opponent.add_death(1)
            self.add_death(1)
            opponent.add_kill(1)
            print(3)
            return 3
