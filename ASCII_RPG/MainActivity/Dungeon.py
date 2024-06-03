import Character

class Dungeon():
    def __init__(self):
        self.name = "Dungeon Name"
        self.rooms = ["Dungeon 1", "Dungeon 2"] 
        self.roomLayout = [[]] # 던전의 레이아웃을 텍스트로 안에 저장. 예를 들어
        '''
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0
        0, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6
        0, 1, 1, 1, 1, 1, 1, 1, 1, 3, 0
        0, 1, 1, 1, 4, 4, 4, 4, 4, 4, 0
        0, 1, 1, 1, 4, 4, 4, 4, 4, 4, 0
        0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0
        '''
        # 이런 식으로, 0은 벽, 1은 땅, 2와 3은 아이템, 4는 지형물, 5는 입구, 6은 출구처럼 던전 맵을 리스트로 아얘 안쪽 배열에 넣어버리기. (추후에 다시 설정해야 함)
        # 새로운 맵을 생성할 시엔 맵을 내부 리스트를 하나 만들어서 넣어주고, 표기는 그 이후에.
        self.currentRoomIndex = 0
        self.character = Character()

    def enter(self):
        # 캐릭터가 들어온 것을 확인, 던전에 따라 currentRoomIndex를 초기화
        return

    def moveToNextRroom():
        # 다음 방의 인덱스를 확인하고 다음 방으로 케릭터를 이동. enter()를 활용.
        return
    
    def generateRandomRoom():
        # 랜덤으로 다음 방을 만들기. 기본 레이아웃 알고리즘은
        # 1. 벽으로 맵이 둘러싸여야 한다.
        # 2. 랜덤한 오브젝트들이 땅에 몇개 정도 너무 많지 않게, 적당히 있어야 한다.
        # 3. 나오는 몬스터의 타입은 레벨에 맞춰 배틀 시스템에서 적당히 배치.(맵에선 구현 X)
        return