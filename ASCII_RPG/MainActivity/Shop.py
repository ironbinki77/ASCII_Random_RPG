import Character, item

character = Character()
inventory = [] # 상점 데이터. 레벨에 따라 자동 조정.

class Shop():
    def __init__(self):
        # 상점 아이템 초기화
        if character.level <= 10 and inventory.len() < 2:
            inventory.append[1, 2]
        elif 10 <= character.level <= 20 and self.inventory.len() < 4:
            inventory.append[3, 4]
        elif 20 <= character.level <= 40 and self.inventory.len() < 7:
            inventory.append[5, 6, 7]
        # ... 등의 방식으로 레벨과 인벤토리에 있는 아이템의 개수를 토대로 측정. 레벨 다운 이벤트가 없기에 예외 처리는 안함.
        # 이 이후 아이템을 사는지, 파는지 선택하게 함

    def buyItem(character, item):
        # 케릭터의 인벤토리, 돈을 확인하고 돈이 충분할 경우 인벤토리에 아이템을 추가하고 돈을 discount 하는 함수 코드.
        return
    
    def sellItem(character, item):
        # 팔 수 있는 아이템인지 확인 후 원본 가격의 일정 배율(예: 0.25x, 0.5x 등)으로 아이템 판매를 진행(-아이템, +돈).
        return
    
    # addItemToShop과 removeItemFromShop은 자동으로 배열을 수정하기에 필요 없음. 상점은 불러와 질 때마다 자동으로 인벤토리를 수정.