import random
class team:

    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def add_hero(self, hero):
        self.heroes.append(hero)
        return

    def remove_hero(self, name):
        found_hero = False
        for hero in self.heroes:
            if hero.name == name:
                found_hero = True
                self.heroes.remove(hero)
        if not found_hero:
            return 0
        return

    def list_heroes(self):
        for hero in self.heroes:
            print(f"Name: {hero}, HP {hero.current_health}")
        return

    def stats(self):
        for hero in self.heroes:
            kd = 0
            if hero.deaths != 0:
                kd = hero.kills / hero.deaths
            print(f"{hero._name} Kill/Deaths: {kd}")
        return
    
    def revive_heroes(self):
        for hero in self.heroes:
            hero.current_health = hero.starting_health
        return
    
    def attack(self, opponents):
        living_heroes = list()
        living_opponents = list()
        
        for hero in self.heroes:
            living_heroes.append(hero)
        
        for hero in opponents.heroes:
            living_opponents.append(hero)
        
        while len(living_heroes) > 0 and len(living_opponents) > 0:
            f1 = random.choice(living_heroes)
            f2 = random.choice(living_opponents)
            x = f1.fight(f2)
            if x == 1:
                living_opponents.remove(f2)
            elif x == 2:
                living_heroes.remove(f1)
            elif x == 3:
                living_heroes.remove(f1)
                living_opponents.remove(f2)
