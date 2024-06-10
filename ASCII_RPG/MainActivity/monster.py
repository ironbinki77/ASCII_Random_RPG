import random

from ASCII_RPG.MainActivity.Character import Character


class monster:
    def __init__(self, name, level, health, attack, defense, gold, loots, dropRate):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense
        self.gold = gold
        self.loot = loots
        self.dropRate = dropRate

    def attack(self, characters):
        damage = self.attack - characters.defense
        if damage > 0:
            characters.takeDamage(damage)
        else:
            characters.takeDamage(1)  # 최소 데미지 1

    def takeDamage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def isDefeated(self):
        return self.health == 0

    def dropLoot(self):
        if random.random() < self.dropRate:
            return random.choice(self.loot)
        return None


class Monster:
    def __init__(self):
        self.name = None

    def attack(self, characters):
        pass

    def takeDamage(self, param):
        pass

    def isDefeated(self):
        pass

    def dropLoot(self):
        pass


Monsters = Monster(
)

character = Character(name="Hero")  

Monsters.attack(character)


Monsters.takeDamage(20)


if Monsters.isDefeated():
    print(f"{Monsters.name} is defeated!")
    loot = Monsters.dropLoot()
    if loot:
        print(f"Dropped item: {loot.name}")
    else:
        print("No item dropped.")
