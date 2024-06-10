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
