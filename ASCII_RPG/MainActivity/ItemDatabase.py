import json
from Item import Item

class ItemDatabase:
    def __init__(self, filename='items.json'):
        self.filename = filename
        self.items = self.load_items()

    def load_items(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            items = {}
            for item_code, item_data in data.items():
                item = Item(
                    name=item_data['name'],
                    description=item_data['description'],
                    buyPrice=item_data['buyPrice'],
                    sellPrice=item_data['sellPrice']
                )
                items[int(item_code)] = item
            return items

    def get_item(self, item_code):
        return self.items.get(item_code, None)