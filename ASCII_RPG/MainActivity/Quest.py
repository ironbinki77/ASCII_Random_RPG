import json

import json

class Quest:
    def __init__(self, questNum, item_database):
        self.item_database = item_database
        self.isCompleted = False
        self.load_quest_data(questNum)

    def load_quest_data(self, questNum):
        # Load quest data from a JSON file
        with open('quests.json', 'r', encoding='utf-8') as file:
            quests = json.load(file)
            quest_data = quests[str(questNum)]

        self.name = quest_data['name']
        self.description = quest_data['description']
        self.requirements = quest_data['requirements']
        self.reward = quest_data['reward']

    def check_complete(self, character):
        req_type, req_code, req_amount = self.requirements
        if req_type == "MonsterKill":
            if character.get_kills(req_code) >= req_amount:
                self.complete_quest(character)
                return True
        elif req_type == "ItemCollected":
            if character.get_item_count(req_code) >= req_amount:
                self.complete_quest(character)
                return True
        elif req_type == "Story":
            self.complete_quest(character)
            return True
        return False

    def complete_quest(self, character):
        if not self.isCompleted:
            exp_reward, gold_reward, item_rewards = self.reward
            character.gainXp(exp_reward)
            character.gold += gold_reward
            for item_code, quantity in item_rewards:
                for _ in range(quantity):
                    item = self.item_database.get_item(item_code)
                    if item:
                        character.addItemToInventory(item)
            self.isCompleted = True
            print(f"Quest '{self.name}' completed!")
        else:
            print(f"Quest '{self.name}' is already completed.")
