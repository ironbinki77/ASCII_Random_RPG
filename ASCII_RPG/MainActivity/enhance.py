import json
from .Item import ItemDatabase
from .Character import Character

class EnhanceSystem:
    def __init__(self, item_db_filename='data/items.json', inventory_filename='data/inventory.json'):
        self.item_db = ItemDatabase(item_db_filename)
        self.inventory_filename = inventory_filename

    def load_inventory(self):
        try:
            with open(self.inventory_filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_inventory(self, inventory):
        with open(self.inventory_filename, 'w', encoding='utf-8') as file:
            json.dump(inventory, file)

    def enhance_item(self, character, item_code):
        inventory = self.load_inventory()

        if item_code not in inventory:
            return {'status': 'failure', 'message': 'Item not found in inventory'}

        item = self.item_db.get_item(item_code)

        if not item:
            return {'status': 'failure', 'message': 'Item not found in item database'}

        enhance_cost = item.enhancementLevel * 10  # Example cost calculation
        if character.gold < enhance_cost:
            return {'status': 'failure', 'message': 'Not enough gold to enhance item'}

        # Deduct gold and enhance the item
        character.gold -= enhance_cost
        item.enhance()

        # Save the enhanced item back to the inventory
        inventory[item_code] = item.__dict__
        self.save_inventory(inventory)

        return {'status': 'success', 'message': f'Item {item.name} enhanced to level {item.enhancementLevel}'}

# Example usage
if __name__ == '__main__':
    item_db_path = 'data/items.json'
    inventory_path = 'data/inventory.json'

    enhance_system = EnhanceSystem(item_db_path, inventory_path)
    character = Character(name="Hero", gold=100)

    # Add an item to the character's inventory for testing
    character.addItemToInventory(enhance_system.item_db.get_item(1))  # Assuming item code 1 exists

    # Enhance the item
    result = enhance_system.enhance_item(character, 1)
    print(result)
