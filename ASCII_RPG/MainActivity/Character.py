import json
import os
from django.conf import settings


class Character:
    file_path = os.path.join(settings.BASE_DIR, 'main_app', 'resources', 'userdata.json')

    with open(file_path, 'r') as file:
        savedata = json.load(file)

    def __init__(self):
        self.name = self.savedata["name"]
        self.level = self.savedata["level"]
        self.gold = self.savedata["gold"]
        self.xp = self.savedata["xp"]
        self.hp = self.savedata["hp"]
        self.max_hp = self.savedata["max_hp"]
        self.mp = self.savedata["mp"]
        self.max_mp = self.savedata["max_mp"]
        self.str = self.savedata["str"]
        self.dex = self.savedata["dex"]
        self.int = self.savedata["int"]
        self.def_s = self.savedata["def"]
        self.luk = self.savedata["luk"]
        self.skills = self.savedata["skills"]
        self.inven = self.savedata["inven"]
        self.equip = self.savedata["equip"]

    def write_data(self):
        if isinstance(self.savedata, dict):
            with open(self.file_path, 'w') as file:
                json.dump(self.savedata, file, indent=2)
            print("Console | File Data Successfully Updated")
        else:
            print("Console | Something is wrong on the data save!")
