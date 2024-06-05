from django.shortcuts import render
from django.http import HttpResponse
from ASCII_RPG.MainActivity import Battle, Character, monster
import random

# Create your views here.

mob_list = [
    monster.monster("Slime", 3, 30, 4, 3, 5, [1], 0.1),
    monster.monster("Zombie", 2, 20, 3, 1, 3, [2], 0.4),
    monster.monster("Goblin", 5, 50, 12, 5, 10, [], 0),
    monster.monster("Skeleton", 3, 25, 7, 1, 7, [], 0),
    monster.monster("Creeper", 1, 10, 20, 0, 5, [], 0)
]

def main(request):
    return render(request, 'main_app/main.html')


def battle_view(request):
    player_o = Character.Character("Player")
    mob_num = int(5 * random.random())
    enemy_o = mob_list[mob_num]

    battle = Battle.Battle(player_o, enemy_o)

    # 세션을 사용하여 battle 객체를 저장하고 관리할 수 있습니다.
    if 'battle' not in request.session:
        request.session['battle'] = battle.__dict__  # 객체 상태를 세션에 저장
    else:
        battle.__dict__.update(request.session['battle'])  # 세션에서 객체 상태 복원

    battle.message = "적" + enemy_o.name + "이 나타났습니다!"

    if request.method == 'POST':
        action = request.POST.get('action')
        if action:
            if action == 'attack':
                battle.message = "공격합니다!"
                if player_o.strength - 0.6 * enemy_o.defense > 0:
                    enemy_o.health = enemy_o.health - (player_o.strength - 0.6 * enemy_o.defense)
            elif action == 'defend':
                battle.message = "방어 태세에 들어갑니다!"
                battle.character_status = 1
            elif action == 'item':
                battle.message = "아이템을 사용합니다!"
            elif action == 'run':
                battle.message = "도망쳤습니다!"
                battle.combatFinished = True
            battle.count += 1  # 턴 증가
        else:
            battle.message = battle.next_turn()
    else:
        battle.message = battle.next_turn()

    # 세션에 battle 객체 상태를 업데이트합니다.
    if not battle.combatFinished:
        request.session['battle'] = battle.to_object()
    else:
        return render(request, 'main_app/main.html')

    context = {
        'message': battle.message,
        'show_menu': battle.count != 0  # self.count가 0이 아닌 경우에만 메뉴 표시
    }
    return render(request, 'main_app/battle.html', context)
