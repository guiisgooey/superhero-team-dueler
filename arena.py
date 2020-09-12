from team import team
from armor import armor
from team import team
from hero import hero
from ability import ability
from weapon import weapon
class arena:
    def __init__(self):
        global team
        self.team_one = team("team one")
        self.team_two = team("team two")

    def create_ability(self):
        global ability
        name = input("What is the ability's name?  ")
        max_damage = int(input("What is the max damage of the ability?  "))
        return ability(name, max_damage)

    def create_weapon(self):
        global weapon
        name = input("What is the weapon name?  ")
        max_damage = int(input("What is the max damage of the weapon?  "))
        return weapon(name, max_damage)

    def create_armor(self):
        global armor
        name = input("What is the armor's name?  ")
        max_block = int(input("What is the max block of the armor?  "))
        return armor(name, max_block)

    def create_hero(self):
        global hero
        hero_name = input("Hero's name: ")
        hero1 = hero(hero_name)
        add_item = None
        while add_item != "4":
           add_item = input(
               "[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
           if add_item == "1":
               x = self.create_ability()
               hero1.add_ability(x)

           elif add_item == "2":
               x = self.create_weapon()
               hero1.add_weapon(x)

           elif add_item == "3":
               x = self.create_armor()
               hero1.add_armor(x)

        return hero1
    
    def build_team_one(self):
        '''Prompt the user to build team_one '''
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        self.team_one.attack(self.team_two)

    def show_stats(self):
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")
        team_kills = 0
        team_deaths = 0

        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))

        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero._name)
        
        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero._name)

