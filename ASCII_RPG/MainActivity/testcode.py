from __future__ import absolute_import


from .Item import Item
from .Character import Character
from .Shop import Shop
from .Inventory import Inventory

def main():
    # Initialize item database and shop
    item_db = ItemDatabase('data/items.json')
    shop = Shop(item_db, 'data/inventory.json')

    # Initialize character
    character = Character(name="Hero", gold=100)

    # Print initial state
    print(f"Initial gold: {character.gold}")
    print(f"Initial inventory: {character.inventory.list_items()}")

    # Attempt to buy an item
    print("\nBuying item 1 (Basic Sword)...")
    shop.buy_item(character, 1)  # Attempt to buy Basic Sword

    # Print state after buying
    print(f"Gold after buying: {character.gold}")
    print(f"Inventory after buying: {character.inventory.list_items()}")

    # Attempt to sell an item
    print("\nSelling item 1 (Basic Sword)...")
    shop.sell_item(character, 1)  # Attempt to sell Basic Sword

    # Print state after selling
    print(f"Gold after selling: {character.gold}")
    print(f"Inventory after selling: {character.inventory.list_items()}")

if __name__ == "__main__":
    main()
