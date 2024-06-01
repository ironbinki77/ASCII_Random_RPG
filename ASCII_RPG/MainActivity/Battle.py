import random

enemyList = []

class Battle():
    def __init__(self, character):
        self.character = character
        self.enemy = int(random.random() * enemyList.len()) - 1 # 적의 개수 중 랜덤하게 골라서 1마리, 추후 케릭터의 레벨에 맞춰 범위를 정할 예정. 적의 코드를 리스트에서 가져올 때 활용.
        # 적이 담긴 리스트는 레벨 순으로, 낮은 순부터 높은 순으로 하여 낮은 적의 코드가 나온 경우(레벨이 낮은 경우) 더 쉬운 몹이 나오게 알고리즘을 설정.
        self.start()
    
    def characterTurn():
        # 케릭터가 턴을 가져갈 때 마다 카운트를 올리고, 카운트에 맞춰 어떤 액션을 할 것인지 받아오기
        return
    def enemyTurn():
        # 적의 턴에 어떤 행동을 적이 할 지 랜덤으로 정하기(스킬의 개수에 맞춰 랜덤으로)
        return
    def checkBattleStatus():
        # 전투가 끝났는지 안 끝났는지 확인, 승패 확인
        return

    def start():
        # characterTurn, enemyTurn, checkBattleStatus를 이용해 배틀을 진행시키는 함수.
        return