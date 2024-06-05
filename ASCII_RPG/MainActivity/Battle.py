import random
import time

enemyList = []

class Battle:
    def __init__(self, character, monster):
        self.character = character
        self.monster = monster
        self.enemy = int(random.random() * 5) - 1 # 적의 개수 중 랜덤하게 골라서 1마리, 추후 케릭터의 레벨에 맞춰 범위를 정할 예정. 적의 코드를 리스트에서 가져올 때 활용.
        # 적이 담긴 리스트는 레벨 순으로, 낮은 순부터 높은 순으로 하여 낮은 적의 코드가 나온 경우(레벨이 낮은 경우) 더 쉬운 몹이 나오게 알고리즘을 설정.
        self.turn = 0
        self.count = 0
        self.character_status = 0 # Defense = 1, Normal = 0
        self.monster_status = 0 # Defense = 1, Normal = 0
        self.combatFinished = False
        self.message = ""

    def to_object(self):
        ret = self.__dict__
        ret["character"] = self.character.__dict__
        ret["monster"] = self.monster.__dict__

    def character_turn(self):
        self.message = "플레이어의 턴입니다. 어떤 선택을 하시겠습니까?"
        self.count += 1
        return self.message

    def enemy_turn(self):
        action = random.choice(["attack", "defend"])
        if action == "attack":
            self.message = "적이 공격해 옵니다!"
            if (self.monster.attack - self.character.defense * 0.8) > 0:
                self.character.health = self.character.health - (self.monster.attack - self.character.defense * 0.8)
        else:
            self.message = "적이 방어를 하고 있습니다!"
            self.monster_status = 1
        self.count += 1
        return self.message

    def start(self):
        if self.turn % 2 == 0:
            return self.character_turn()
        else:
            return self.enemy_turn()

        # character_turn, enemy_turn을 이용해 배틀을 진행시키는 함수.'

    def next_turn(self):
        self.turn += 1
        return self.start()
