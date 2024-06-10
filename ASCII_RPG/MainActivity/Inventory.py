import json

class Inventory:
    def __init__(self, filename='inventory.json'):
        self.filename = filename
        self.items = self.load_inventory()

    def load_inventory(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_inventory(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.items, file)

    def add_item(self, item_code):
        if item_code in self.items:
            self.items[item_code] += 1
        else:
            self.items[item_code] = 1
        self.save_inventory()

    def remove_item(self, item_code):
        if item_code in self.items:
            if self.items[item_code] > 1:
                self.items[item_code] -= 1
            else:
                del self.items[item_code]
            self.save_inventory()

    def get_item_count(self, item_code):
        return self.items.get(item_code, 0)

    def list_items(self):
        return self.items
