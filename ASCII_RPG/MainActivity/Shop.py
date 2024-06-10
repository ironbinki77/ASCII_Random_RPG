from .Character import Character
from .Inventory import Inventory
import Item

class Shop:
    def __init__(self, item_database, inventory_filename):
        self.item_database = item_database
        self.inventory_filename = inventory_filename

    def buy_item(self, character, item_code):
        item = self.item_database.get_item(item_code)
        if item and character.gold >= item.buyPrice:
            character.gold -= item.buyPrice
            character.addItemToInventory(item)
            print(f"Bought {item.name} for {item.buyPrice} gold.")
        else:
            print("Not enough gold or item not found.")

    def sell_item(self, character, item_code):
        item = self.item_database.get_item(item_code)
        if item and item_code in character.inventory.list_items():
            character.gold += item.sellPrice
            character.removeItemFromInventory(item)
            print(f"Sold {item.name} for {item.sellPrice} gold.")
        else:
            print("Item not found in inventory.")
