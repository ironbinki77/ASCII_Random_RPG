class Skill:
    def __init__(self, name, description, manaCost, effectType, effectAmount, cooldown):
        self.name = name
        self.description = description
        self.manaCost = manaCost
        self.effectType = effectType
        self.effectAmount = effectAmount
        self.currentCooldown = 0
        self.cooldown = cooldown

    def use(self, character):
        if self.isAvailable() and character.useMana(self.manaCost):
            self.currentCooldown = self.cooldown
            if self.effectType == "damage":
                return self.effectAmount
            elif self.effectType == "heal":
                character.health += self.effectAmount
                if character.health > character.maxHealth:
                    character.health = character.maxHealth
            return True
        return False

    def isAvailable(self):
        return self.currentCooldown == 0

    def reduceCooldown(self):
        if self.currentCooldown > 0:
            self.currentCooldown -= 1

