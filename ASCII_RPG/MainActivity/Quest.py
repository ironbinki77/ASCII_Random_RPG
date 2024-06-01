class Quest():
    def __init__(self, questNum):
    # 미리 정해져 있는 .json 파일 혹은 퀘스트 DB에서 퀘스트 데이터를 불러 와 각 변수에 대입하는 방식으로 진행. 아래는 데이터 대입 시를 예시로 만든 데이터.
        self.name = "Temp Quest: Kill Slimes" # String 타입
        self.description = "Temp Quest Description: Kill 10 Slimes" # String 타입
        self.requirements = ["MonsterKill", 1, 10] # 첫 번째 값은 타입("MonsterKill", "ItemCollected" 등, "Story"일 시 스토리 퀘스트로 판정 및 모든 값 0), 두 번째 값은 개체 코드(몬스터, 아이템 등의 식별 코드), 세 번째 값은 개수
        self.reward = [10, 100, [1, 1]] # 첫 번째 값은 경험치, 두 번째는 골드, 세 번째 이후로는 아이템 코드에 맞춘 아이템 배분 - 없을 시 아이템 X
        self.isCompleted = False # 성공 시 True로 변경.

    def checkComplete(character):
        # requirements에 character의 Inventory, Money, EXP 등 이 중 특정 조건이 만족되었는지 확인한 후, Quest를 완료시킨다. 아닐 경우, 아니라고 Return한다(아마 0으로 Return하면 될 듯).
        return