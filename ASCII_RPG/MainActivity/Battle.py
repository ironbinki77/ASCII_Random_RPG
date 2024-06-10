import random
from .Character import Character
from .Monster import Monster

class Battle:
    def __init__(self):
        self.character = Character()
        mob_tag = str(random.randint(1, 6))
        self.monster = Monster(mob_tag)
        self.turn = 0
        self.combatFinished = False
        self.message = ""

    def player_attack(self):
        damage = max(self.character.str - self.monster.def_s, 0)
        self.monster.hp -= damage
        self.message = f"{self.character.name} attacks {self.monster.name} for {damage} damage!"
        if self.monster.hp <= 0:
            self.message += f" {self.monster.name} has been defeated!"
            self.combatFinished = True

    def monster_attack(self):
        damage = max(self.monster.atk - self.character.def_s, 0)
        self.character.hp -= damage
        self.message = f"{self.monster.name} attacks {self.character.name} for {damage} damage!"
        if self.character.hp <= 0:
            self.message += f" {self.character.name} has been defeated!"
            self.combatFinished = True

    def player_turn(self, action):
        if not self.combatFinished:
            if action == 'attack':
                self.player_attack()
            elif action == 'defend':
                self.message = "Player defends!"
                # Implement defend logic here
            elif action == 'item':
                self.message = "Player uses an item!"
                # Implement item usage logic here
            elif action == 'run':
                self.message = "Player runs away!"
                self.combatFinished = True

            if not self.combatFinished and action != 'run':
                self.turn += 1
                if self.turn % 2 == 1:  # Monster's turn
                    self.monster_attack()
