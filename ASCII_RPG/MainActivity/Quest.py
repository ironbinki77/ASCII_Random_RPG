import json


class Quest:
    def __init__(self, questNum, item_database, character):
        self.reward = None
        self.requirements = None
        self.description = None
        self.name = None
        self.item_database = item_database
        self.character = character
        self.isCompleted = False
        self.load_quest_data(questNum)

    def load_quest_data(self, questNum):
        with open('quests.json', 'r', encoding='utf-8') as file:
            quests = json.load(file)
            quest_data = quests[str(questNum)]

        self.name = quest_data['name']
        self.description = quest_data['description']
        self.requirements = quest_data['requirements']
        self.reward = quest_data['reward']

    def check_complete(self):
        req_type, req_code, req_amount = self.requirements
        if req_type == "MonsterKill":
            if self.character.get_kills(req_code) >= req_amount:
                self.complete_quest()
                return True
        elif req_type == "ItemCollected":
            if self.character.get_item_count(req_code) >= req_amount:
                self.complete_quest()
                return True
        elif req_type == "Story":
            self.complete_quest()
            return True
        return False

    def complete_quest(self):
        if not self.isCompleted:
            exp_reward, gold_reward, item_rewards = self.reward
            self.character.gainXp(exp_reward)
            self.character.gold += gold_reward
            for item_code, quantity in item_rewards:
                for _ in range(quantity):
                    item = self.item_database.get_item(item_code)
                    if item:
                        self.character.addItemToInventory(item)
            self.isCompleted = True
            print(f"Quest '{self.name}' completed!")
        else:
            print(f"Quest '{self.name}' is already completed.")
