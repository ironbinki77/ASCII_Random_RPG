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
        self.inventory = []
        self.equipment = []

    def gainXp(self, amount):
        self.currentXp += amount
        while self.currentXp >= self.xpToNextLevel:
            self.levelUp()

    def levelUp(self):
        self.level += 1
        self.currentXp -= self.xpToNextLevel
        self.xpToNextLevel = int(self.xpToNextLevel * 1.5)  # Example: Increase XP needed for next level
        self.maxHealth += 10
        self.health = self.maxHealth
        self.maxMana += 5
        self.mana = self.maxMana
        self.strength += 2
        self.dexterity += 2
        self.intelligence += 2
        self.defense += 2
        self.luck += 1

    def takeDamage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def useMana(self, amount):
        if self.mana >= amount:
            self.mana -= amount
            return True
        else:
            return False

    def learnSkill(self, skill):
        self.skills.append(skill)

    def equipItem(self, item):
        if not item.isEquipped:
            self.equipment.append(item)
            item.isEquipped = True

    def unequipItem(self, item):
        if item in self.equipment:
            self.equipment.remove(item)
            item.isEquipped = False

    def addItemToInventory(self, item):
        self.inventory.append(item)

    def removeItemFromInventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
