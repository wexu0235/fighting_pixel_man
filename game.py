# game.py
import random
from player import Player
from ascii import ascii, print_side_by_side

# Restraint relationship table
element_counter = {
    'Earth': 'Water',
    'Water': 'Fire',
    'Fire': 'Earth'
}

def is_countered(attacker: Player, defender: Player) -> bool:
    return element_counter.get(attacker.element) == defender.element

def give_element_hint(attacker: Player, defender: Player):
    if is_countered(attacker, defender):
        print("🗡You have elemental advantage! Strike now!")
    elif is_countered(defender, attacker):
        print("🛡Be careful! Opponent has elemental advantage!")

def format_bar(current, maximum=10, length=10):
    percent = max(0, current / maximum)
    filled = int(percent * length)
    empty = length - filled
    bar = '█' * filled + '▒' * empty
    percentage = int(percent * 100)
    return f"[{bar}] {percentage}%"

def show_status_summary(player: Player, pc: Player):
    print(f"{'-'*70}")
    print(f"{'STATUS SUMMARY':^70}")
    print(f"{'-'*70}")
    print(f"{player.name:<35}{pc.name}")
    print(f"HP:     {format_bar(player.hp):<27}HP:     {format_bar(pc.hp)}")
    print(f"Energy: {format_bar(player.energy):<27}Energy: {format_bar(pc.energy)}")
    print(f"Element: {player.element:<26}Element: {pc.element}")
    print()

def start_battle(player: Player, pc: Player):
    print("⚔ Battle Start!")
    show_status_summary(player, pc)

    while player.is_alive() and pc.is_alive():
        give_element_hint(player, pc)

        # The player selects the action.
        player_action = player.choose_action()

        # AI Randomly select the action
        actions = ['normal_attack', 'element_attack', 'special_attack', 'defend', 'reflect']
        pc_choices = [a for a in actions if pc.can_use(a)]
        if (is_countered(player, pc) or pc.element == player.element) and 'element_attack' in pc_choices:
            pc_choices.remove('element_attack')
        pc_action = random.choice(pc_choices)
        pc.consume_energy(pc_action)

        # Calculate damage
        def get_attack_damage(attacker, action, defender):
            if action == 'normal_attack':
                return 1
            elif action == 'element_attack':
                if is_countered(attacker, defender):
                    return 2
                else:
                    return 1
            elif action == 'special_attack':
                return 4
            return 0

        p1_dmg = get_attack_damage(player, player_action, pc)
        p2_dmg = get_attack_damage(pc, pc_action, player)

        # Defense/Rebound
        def apply_defense(defender, dmg, attacker):
            if is_countered(attacker, defender):
                return max(dmg - 2, 0)
            return max(dmg - 1, 0)

        if player_action == 'defend':
            p2_dmg = apply_defense(player, p2_dmg, pc)
            p1_dmg = 0
        elif player_action == 'reflect':
            p1_dmg = p2_dmg
            p2_dmg = 0

        if pc_action == 'defend':
            p1_dmg = apply_defense(pc, p1_dmg, player)
            p2_dmg = 0
        elif pc_action == 'reflect':
            p2_dmg = p1_dmg
            p1_dmg = 0

        # If both sides defend or rebound, there will be no damage
        if player_action in ['defend', 'reflect'] and pc_action in ['defend', 'reflect']:
            print("🔁 Both players defended or reflected. Nothing happened.")
        else:
            # Application damage
            player.hp = max(0, player.hp - p2_dmg)
            pc.hp = max(0, pc.hp - p1_dmg)

            # Display the round action diagram
            print(f"\n{player.name} took {p2_dmg} damage. Remaining HP: {player.hp}")
            print(f"{pc.name} took {p1_dmg} damage. Remaining HP: {pc.hp}")
        print()
        print_side_by_side(
                getattr(ascii, player_action, ascii.initial),
                getattr(ascii, f"pc_{pc_action}", ascii.initial),
                player.name+'█'*player.hp+'▒'*(10-player.hp)+str(player.hp*10)+'%', 
                pc.name+'█'*pc.hp+'▒'*(10-pc.hp)+str(pc.hp*10)+'%'
        )

        # Restore energy at the end of the round
        player.restore_energy()
        pc.restore_energy()

        # show status
        print("\n🧠 Round Status:")
        show_status_summary(player, pc)

        # Judge the winner or loser
        if not player.is_alive() and not pc.is_alive():
            print("\n🤝 It's a draw!")
            player.record_result("draw")
            print(ascii.initial)
            return
        elif not player.is_alive():
            print(f"\n💀 {player.name} has fallen. PC wins!")
            player.record_result("loss")
            print(ascii.fall)
            return
        elif not pc.is_alive():
            print(f"\n🏆 {player.name} wins the battle!")
            player.record_result("win")
            print(ascii.win)
            return

