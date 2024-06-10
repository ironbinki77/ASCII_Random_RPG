from django.shortcuts import render, redirect
from django.http import JsonResponse
from ASCII_RPG.MainActivity.Character import Character
from ASCII_RPG.MainActivity.Monster import Monster
from ASCII_RPG.MainActivity.Battle import Battle


def main(request):
    return render(request, 'main_app/main.html')


def start_battle(request):
    if 'battle_c_name' not in request.session:
        battle = Battle()
        save_battle_to_session(request, battle)
    else:
        battle = load_battle_from_session(request)

    return battle


def battle_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        battle = load_battle_from_session(request)
        battle.player_turn(action)
        save_battle_to_session(request, battle)

        return JsonResponse({
            'message': battle.message,
            'player_hp': battle.character.hp,
            'enemy_hp': battle.monster.hp,
            'enemy_name': battle.monster.name,
            'show_menu': not battle.combatFinished
        })

    if 'battle_c_name' not in request.session:
        start_battle(request)

    battle = load_battle_from_session(request)
    return render(request, 'main_app/battle.html', {
        'message': battle.message,
        'player_hp': battle.character.hp,
        'enemy_hp': battle.monster.hp,
        'enemy_name': battle.monster.name,
        'show_menu': not battle.combatFinished
    })


def save_battle_to_session(request, battle):
    request.session['battle_c_name'] = battle.character.name
    request.session['battle_c_level'] = battle.character.level
    request.session['battle_c_gold'] = battle.character.gold
    request.session['battle_c_xp'] = battle.character.xp
    request.session['battle_c_hp'] = battle.character.hp
    request.session['battle_c_max_hp'] = battle.character.max_hp
    request.session['battle_c_mp'] = battle.character.mp
    request.session['battle_c_max_mp'] = battle.character.max_mp
    request.session['battle_c_str'] = battle.character.str
    request.session['battle_c_dex'] = battle.character.dex
    request.session['battle_c_int'] = battle.character.int
    request.session['battle_c_def'] = battle.character.def_s
    request.session['battle_c_luk'] = battle.character.luk
    request.session['battle_c_skills'] = battle.character.skills
    request.session['battle_c_inven'] = battle.character.inven
    request.session['battle_c_equip'] = battle.character.equip
    request.session['battle_m_name'] = battle.monster.name
    request.session['battle_m_level'] = battle.monster.level
    request.session['battle_m_hp'] = battle.monster.hp
    request.session['battle_m_max_hp'] = battle.monster.max_hp
    request.session['battle_m_atk'] = battle.monster.atk
    request.session['battle_m_def'] = battle.monster.def_s
    request.session['battle_m_gold'] = battle.monster.gold
    request.session['battle_m_loot'] = battle.monster.loot
    request.session['battle_m_rate'] = battle.monster.rate
    request.session['battle_turn'] = battle.turn
    request.session['battle_combatFinished'] = battle.combatFinished
    request.session['battle_message'] = battle.message


def load_battle_from_session(request):
    battle = Battle()
    battle.character.name = request.session['battle_c_name']
    battle.character.level = request.session['battle_c_level']
    battle.character.gold = request.session['battle_c_gold']
    battle.character.xp = request.session['battle_c_xp']
    battle.character.hp = request.session['battle_c_hp']
    battle.character.max_hp = request.session['battle_c_max_hp']
    battle.character.mp = request.session['battle_c_mp']
    battle.character.max_mp = request.session['battle_c_max_mp']
    battle.character.str = request.session['battle_c_str']
    battle.character.dex = request.session['battle_c_dex']
    battle.character.int = request.session['battle_c_int']
    battle.character.def_s = request.session['battle_c_def']
    battle.character.luk = request.session['battle_c_luk']
    battle.character.skills = request.session['battle_c_skills']
    battle.character.inven = request.session['battle_c_inven']
    battle.character.equip = request.session['battle_c_equip']
    battle.monster.name = request.session['battle_m_name']
    battle.monster.level = request.session['battle_m_level']
    battle.monster.hp = request.session['battle_m_hp']
    battle.monster.max_hp = request.session['battle_m_max_hp']
    battle.monster.atk = request.session['battle_m_atk']
    battle.monster.def_s = request.session['battle_m_def']
    battle.monster.gold = request.session['battle_m_gold']
    battle.monster.loot = request.session['battle_m_loot']
    battle.monster.rate = request.session['battle_m_rate']
    battle.turn = request.session['battle_turn']
    battle.combatFinished = request.session['battle_combatFinished']
    battle.message = request.session['battle_message']
    return battle
