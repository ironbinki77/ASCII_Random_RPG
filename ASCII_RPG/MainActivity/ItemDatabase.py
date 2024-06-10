from Item import Item

class ItemDatabase:
    def __init__(self):
        self.items = self.load_items()

    def load_items(self):
        items = {
            1: Item(name="Basic Sword", description="A simple sword", type="Weapon", strengthPower=5, buyPrice=10, sellPrice=5),
            2: Item(name="Basic Shield", description="A simple shield", type="Armor", defensePower=5, buyPrice=15, sellPrice=7.5),
            3: Item(name="Advanced Sword", description="A better sword", type="Weapon", strengthPower=10, buyPrice=30, sellPrice=15),
            4: Item(name="Advanced Shield", description="A better shield", type="Armor", defensePower=10, buyPrice=35, sellPrice=17.5),
            5: Item(name="Expert Sword", description="A high-quality sword", type="Weapon", strengthPower=15, buyPrice=50, sellPrice=25),
            6: Item(name="Expert Shield", description="A high-quality shield", type="Armor", defensePower=15, buyPrice=55, sellPrice=27.5),
            7: Item(name="Magic Wand", description="A wand for casting spells", type="Weapon", intelligencePower=20, buyPrice=60, sellPrice=30)
            # Add more items as needed
        }
        return items

    def get_item(self, item_code):
        return self.items.get(item_code, None)
