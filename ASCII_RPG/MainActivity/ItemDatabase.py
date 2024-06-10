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
                    type=item_data['type'],
                    healthPower=item_data.get('healthPower', 0),
                    manaPower=item_data.get('manaPower', 0),
                    strengthPower=item_data.get('strengthPower', 0),
                    dexterityPower=item_data.get('dexterityPower', 0),
                    intelligencePower=item_data.get('intelligencePower', 0),
                    defensePower=item_data.get('defensePower', 0),
                    luckPower=item_data.get('luckPower', 0),
                    healthBoost=item_data.get('healthBoost', 0),
                    manaBoost=item_data.get('manaBoost', 0),
                    buyPrice=item_data['buyPrice'],
                    sellPrice=item_data['sellPrice']
                )
                items[int(item_code)] = item
            return items

    def get_item(self, item_code):
        return self.items.get(item_code, None)