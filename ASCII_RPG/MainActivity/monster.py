import random

class Monster:
    def __init__(self, name, level, health, attack, defense, gold, loot, dropRate):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense
        self.gold = gold
        self.loot = loot
        self.dropRate = dropRate

    def attack(self, character):
        damage = self.attack - character.defense
        if damage > 0:
            character.takeDamage(damage)
        else:
            character.takeDamage(1)  # 최소 데미지 1

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

monster = Monster(
    name="Goblin",
    level=5,
    health=50,
    attack=12,
    defense=5,
    gold=10,
    loot=[item1, item2], 
    dropRate=0.5  
)

character = Character(name="Hero")  

monster.attack(character)


monster.takeDamage(20)


if monster.isDefeated():
    print(f"{monster.name} is defeated!")
    loot = monster.dropLoot()
    if loot:
        print(f"Dropped item: {loot.name}")
    else:
        print("No item dropped.")
