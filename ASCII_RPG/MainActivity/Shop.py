import json


class Shop:
    def __init__(self, item_database, inventory_file='data/inventory.json'):
        self.item_database = item_database
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        try:
            with open(self.inventory_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_inventory(self):
        with open(self.inventory_file, 'w', encoding='utf-8') as file:
            json.dump(self.inventory, file)

    def list_items(self):
        return self.item_database.items

    def buy_item(self, character, item_code):
        item = self.item_database.get_item(item_code)
        if item and character.gold >= item.buyPrice:
            character.gold -= item.buyPrice
            character.addItemToInventory(item)
            self.save_inventory()
            return True
        return False

    def sell_item(self, character, item_code):
        item = self.item_database.get_item(item_code)
        if item and character.get_item_count(item_code) > 0:
            character.gold += item.sellPrice
            character.removeItemFromInventory(item)
            self.save_inventory()
            return True
        return False
