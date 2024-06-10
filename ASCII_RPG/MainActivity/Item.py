import json

class Item:
    def __init__(self, item_code, name, description, item_type, stats=None, boosts=None, isEquipped=False, enhancementLevel=0, buyPrice=0, sellPrice=0):
        self.item_code = item_code
        self.name = name
        self.description = description
        self.item_type = item_type
        self.stats = stats if stats else {'healthPower': 0, 'manaPower': 0, 'strengthPower': 0, 'dexterityPower': 0, 'intelligencePower': 0, 'defensePower': 0, 'luckPower': 0}
        self.boosts = boosts if boosts else {'healthBoost': 0, 'manaBoost': 0}
        self.isEquipped = isEquipped
        self.enhancementLevel = enhancementLevel
        self.buyPrice = buyPrice
        self.sellPrice = sellPrice

    def use(self, character):
        if self.item_type == "Consumable":
            character.apply_boosts(self.boosts)
            return True
        return False

    def enhance(self):
        self.enhancementLevel += 1
        self.stats['healthPower'] += 5
        self.stats['manaPower'] += 5
        self.stats['strengthPower'] += 2
        self.stats['dexterityPower'] += 2
        self.stats['intelligencePower'] += 2
        self.stats['defensePower'] += 2
        self.stats['luckPower'] += 1


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
                    item_code=int(item_code),
                    name=item_data['name'],
                    description=item_data['description'],
                    item_type=item_data['type'],
                    stats={
                        'healthPower': item_data.get('healthPower', 0),
                        'manaPower': item_data.get('manaPower', 0),
                        'strengthPower': item_data.get('strengthPower', 0),
                        'dexterityPower': item_data.get('dexterityPower', 0),
                        'intelligencePower': item_data.get('intelligencePower', 0),
                        'defensePower': item_data.get('defensePower', 0),
                        'luckPower': item_data.get('luckPower', 0)
                    },
                    boosts={
                        'healthBoost': item_data.get('healthBoost', 0),
                        'manaBoost': item_data.get('manaBoost', 0)
                    },
                    buyPrice=item_data['buyPrice'],
                    sellPrice=item_data['sellPrice']
                )
                items[int(item_code)] = item
            return items

    def get_item(self, item_code):
        return self.items.get(item_code, None)
