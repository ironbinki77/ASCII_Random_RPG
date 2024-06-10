from Character import Character
from Item import Item

class Shop:
    def __init__(self, character):
        self.character = character
        self.inventory = self.initialize_inventory(character.level)

    def initialize_inventory(self, level):
        inventory = []
        if level <= 10:
            inventory.extend([
                Item(name="Basic Sword", description="A simple sword", type="Weapon", strengthPower=5, buyPrice=10, sellPrice=5),
                Item(name="Basic Shield", description="A simple shield", type="Armor", defensePower=5, buyPrice=15, sellPrice=7.5)
            ])
        elif 10 < level <= 20:
            inventory.extend([
                Item(name="Advanced Sword", description="A better sword", type="Weapon", strengthPower=10, buyPrice=30, sellPrice=15),
                Item(name="Advanced Shield", description="A better shield", type="Armor", defensePower=10, buyPrice=35, sellPrice=17.5)
            ])
        elif 20 < level <= 40:
            inventory.extend([
                Item(name="Expert Sword", description="A high-quality sword", type="Weapon", strengthPower=15, buyPrice=50, sellPrice=25),
                Item(name="Expert Shield", description="A high-quality shield", type="Armor", defensePower=15, buyPrice=55, sellPrice=27.5),
                Item(name="Magic Wand", description="A wand for casting spells", type="Weapon", intelligencePower=20, buyPrice=60, sellPrice=30)
            ])
        # Add more conditions as needed
        return inventory

    def buy_item(self, item_name):
        item = next((i for i in self.inventory if i.name == item_name), None)
        if item and self.character.gold >= item.buyPrice:
            self.character.addItemToInventory(item)
            self.character.gold -= item.buyPrice
            self.inventory.remove(item)
            print(f"Bought {item.name} for {item.buyPrice} gold.")
        else:
            print("Cannot buy the item.")

    def sell_item(self, item_name):
        item = next((i for i in self.character.inventory if i.name == item_name), None)
        if item:
            self.character.removeItemFromInventory(item)
            self.character.gold += item.sellPrice
            print(f"Sold {item.name} for {item.sellPrice} gold.")
        else:
            print("Cannot sell the item.")

# Example usage
character = Character(name="Hero", level=15, gold=100)
shop = Shop(character)

# Assuming the character tries to buy and sell an item by name
shop.buy_item("Basic Sword")
shop.sell_item("Basic Sword")
