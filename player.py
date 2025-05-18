# player.py
from ascii import ascii

class Player:
    
    def __init__(self, name: str, element: str):
        self.name = name
        self.element = element.capitalize()
        if element not in ['Water', 'Fire', 'Earth']:
            raise ValueError("Invalid element. Choose from Water, Fire, Earth.")
        self.hp = 10
        self.energy = 10
        self.battles = 0
        self.wins = 0
        self.losses = 0
        self.draws = 0
   
    def is_alive(self):
        return self.hp > 0

    def restore_energy(self):
        self.energy = min(self.energy + 1, 10)

    def can_use(self, move):
        cost = {
            'normal_attack': 0,
            'element_attack': 2,
            'special_attack': 5,
            'defend': 2,
            'reflect': 3
        }
        return self.energy >= cost[move]

    def consume_energy(self, move):
        cost = {
            'normal_attack': 0,
            'element_attack': 2,
            'special_attack': 5,
            'defend': 2,
            'reflect': 3
        }
        self.energy -= cost[move]

    def choose_action(self):
        # print(f"{self.name}'s Energy: {self.energy}, HP: {self.hp}")
        print('''Choose your action:
        1. Normal Attack|0
        2. Element Attack|2
        3. Special Attack|5
        4. Defend|2
        5. Reflect|3''')
        while True:
            try:
                choice = int(input("> "))
                mapping = {
                    1: 'normal_attack',
                    2: 'element_attack',
                    3: 'special_attack',
                    4: 'defend',
                    5: 'reflect'
                }
                action = mapping.get(choice)
                if not action:
                    raise ValueError
                if self.can_use(action):
                    self.consume_energy(action)
                    return action
                else:
                    print("Not enough energy!")
            except:
                print("Invalid input.")


    def __str__(self):
        return f'''show player - {self.name}
🔋 HP   : {self.hp}% ⚡ Energy: {self.energy}/10 🌟 Element: {self.element}
'''

    def record_result(self, outcome: str):
        if outcome == "win":
            self.wins += 1
        elif outcome == "loss":
            self.losses += 1
        elif outcome == "draw":
            self.draws += 1

    def show_stats(self):
        print(f"\n📊 {self.name}'s Battle Stats")
        print("-----------------------------")
        print(f"Wins   : {self.wins}")
        print(f"Losses : {self.losses}")
        print(f"Draws  : {self.draws}")
        total = self.wins + self.losses + self.draws
        if total:
            rate = self.wins / total * 100
            print(f"Win Rate: {rate:.2f}%")
        else:
            print("Win Rate: N/A")
        print("-----------------------------\n")
