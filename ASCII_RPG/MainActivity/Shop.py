from Item import ItemDatabase
from Character import Character

class Shop:
    def __init__(self, item_database, inventory_file='inventory.json'):
        self.item_database = item_database
        self.inventory = Inventory(filename=inventory_file)

    def buy_item(self, character, item_code):
        item = self.item_database.get_item(item_code)
        if item and character.gold >= item.buyPrice:
            character.gold -= item.buyPrice
            character.addItemToInventory(item)
            print(f"{character.name} bought {item.name} for {item.buyPrice} gold.")
        else:
            print(f"{character.name} does not have enough gold to buy {item.name}.")

    def sell_item(self, character, item_code):
        item = self.item_database.get_item(item_code)
        if item and character.get_item_count(item_code) > 0:
            character.gold += item.sellPrice
            character.removeItemFromInventory(item)
            print(f"{character.name} sold {item.name} for {item.sellPrice} gold.")
        else:
            print(f"{character.name} does not have {item.name} in inventory to sell.")

if __name__ == "__main__":
    item_db = ItemDatabase('items.json')
    shop = Shop(item_db, 'inventory.json')

    # Initialize character
    character = Character(name="Hero", gold=100)

    # Buy and sell items
    shop.buy_item(character, 1)  # Attempt to buy Basic Sword
    shop.sell_item(character, 1)  # Attempt to sell Basic Sword

    # Check character's gold and inventory
    print(f"{character.name} has {character.gold} gold.")
    print(f"{character.name}'s inventory: {character.inventory.list_items()}")
