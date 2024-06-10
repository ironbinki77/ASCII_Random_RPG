from django.shortcuts import render
from django.http import JsonResponse
import json
import os
from MainActivity.Character import Character
from MainActivity.enhance import EnhanceSystem
from MainActivity.Shop import Shop

def main(request):
    return render(request, 'main_app/main.html')

def load_inventory(request):
    inventory_path = os.path.join(os.path.dirname(__file__), 'MainActivity', 'data', 'inventory.json')
    with open(inventory_path, 'r', encoding='utf-8') as file:
        inventory_data = json.load(file)
    return JsonResponse(inventory_data)

def load_shop_items(request):
    items_path = os.path.join(os.path.dirname(__file__), 'MainActivity', 'data', 'items.json')
    with open(items_path, 'r', encoding='utf-8') as file:
        items_data = json.load(file)
    return JsonResponse(items_data)

def buy_item(request, item_code):
    character = Character(name="Hero", gold=100)  # Example character; you should load the actual character data
    shop = Shop(item_db, 'data/inventory.json')
    
    result = shop.buy_item(character, item_code)
    return JsonResponse(result)


def sell_item(request, item_code):
    character = Character(name="Hero", gold=100)  # Example character; you should load the actual character data
    shop = Shop(item_db, 'data/inventory.json')

    result = shop.sell_item(character, item_code)
    return JsonResponse(result)


def load_quests(request):
    quests_path = os.path.join(os.path.dirname(__file__), 'MainActivity', 'data', 'quests.json')
    with open(quests_path, 'r', encoding='utf-8') as file:
        quests_data = json.load(file)
    return JsonResponse(quests_data)

def enhance_item(request, item_code):
    character = Character(name="Hero", gold=100)  # Example character; you should load the actual character data
    enhance_system = EnhanceSystem()

    result = enhance_system.enhance_item(character, item_code)
    return JsonResponse(result)


