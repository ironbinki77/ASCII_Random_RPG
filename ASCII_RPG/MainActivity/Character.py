from Inventory import Inventory

class Character:
    def __init__(self, name, level=1, gold=0, currentXp=0, xpToNextLevel=100, health=100, maxHealth=100, mana=50, maxMana=50, strength=10, dexterity=10, intelligence=10, defense=10, luck=5):
        self.name = name
        self.level = level
        self.gold = gold
        self.currentXp = currentXp
        self.xpToNextLevel = xpToNextLevel
        self.health = health
        self.maxHealth = maxHealth
        self.mana = mana
        self.maxMana = maxMana
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.defense = defense
        self.luck = luck
        self.skills = []
        self.inventory = Inventory()

    def gainXp(self, amount):
        self.currentXp += amount
        while self.currentXp >= self.xpToNextLevel:
            self.levelUp()

    def levelUp(self):
        self.level += 1
        self.currentXp -= self.xpToNextLevel
        self.xpToNextLevel = int(self.xpToNextLevel * 1.5)
        self.maxHealth += 10
        self.health = self.maxHealth
        self.maxMana += 5
        self.mana = self.maxMana
        self.strength += 2
        self.dexterity += 2
        self.intelligence += 2
        self.defense += 2
        self.luck += 1

    def get_kills(self, monster_code):
        return self.kills.get(monster_code, 0)

    def get_item_count(self, item_code):
        return self.inventory.get_item_count(item_code)

    def addItemToInventory(self, item):
        self.inventory.add_item(item.item_code)

    def removeItemFromInventory(self, item):
        self.inventory.remove_item(item.item_code)

    def apply_boosts(self, boosts):
        self.health += boosts['healthBoost']
        if self.health > self.maxHealth:
            self.health = self.maxHealth
        self.mana += boosts['manaBoost']
        if self.mana > self.maxMana:
            self.mana = self.maxMana
