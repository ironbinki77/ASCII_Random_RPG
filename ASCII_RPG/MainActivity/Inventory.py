<<<<<<< Updated upstream
import json
class Inventory:
    def __init__(self, filename='data/inventory.json'):
        self.filename = filename
        self.items = self.load_inventory()

    def load_inventory(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_inventory(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.items, file, indent=4)

    def add_item(self, item_code):
        self.items.append(item_code)
        self.save_inventory()

    def remove_item(self, item_code):
        if item_code in self.items:
            self.items.remove(item_code)
            self.save_inventory()

    def list_items(self):
        return self.items

    def get_item_count(self, item_code):
        return self.items.count(item_code)
=======
class Item:
    def __init__(self, name, description, type, healthPower=0, manaPower=0, strengthPower=0, dexterityPower=0, intelligencePower=0, defensePower=0, luckPower=0, healthBoost=0, manaBoost=0, isEquipped=False, enhancementLevel=0, buyPrice=0, sellPrice=0):
        self.name = name
        self.description = description
        self.type = type
        self.healthPower = healthPower
        self.manaPower = manaPower
        self.strengthPower = strengthPower
        self.dexterityPower = dexterityPower
        self.intelligencePower = intelligencePower
        self.defensePower = defensePower
        self.luckPower = luckPower
        self.healthBoost = healthBoost
        self.manaBoost = manaBoost
        self.isEquipped = isEquipped
        self.enhancementLevel = enhancementLevel
        self.buyPrice = buyPrice
        self.sellPrice = sellPrice

    def use(self, character):
        if self.type == "소모품":
            character.health += self.healthBoost
            if character.health > character.maxHealth:
                character.health = character.maxHealth
            character.mana += self.manaBoost
            if character.mana > character.maxMana:
                character.mana = character.maxMana
            return True
        return False

    def enhance(self):
        self.enhancementLevel += 1
        self.healthPower += 5
        self.manaPower += 5
        self.strengthPower += 2
        self.dexterityPower += 2
        self.intelligencePower += 2
        self.defensePower += 2
        self.luckPower += 1
>>>>>>> Stashed changes
