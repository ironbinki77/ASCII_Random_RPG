import json
import os
from django.conf import settings


class Monster:
    file_path = os.path.join(settings.BASE_DIR, 'main_app', 'resources', 'monsters.json')

    with open(file_path, "r") as file:
        mob_data = json.load(file)

    def __init__(self, tag):
        self.name = self.mob_data[tag]["name"]
        self.level = self.mob_data[tag]["level"]
        self.hp = self.mob_data[tag]["hp"]
        self.max_hp = self.mob_data[tag]["max_hp"]
        self.atk = self.mob_data[tag]["atk"]
        self.def_s = self.mob_data[tag]["def"]
        self.gold = self.mob_data[tag]["gold"]
        self.loot = self.mob_data[tag]["loot"]
        self.rate = self.mob_data[tag]["rate"]
