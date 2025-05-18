# main.py
from player import Player
from game import start_battle

def menu():
    print("""
    ==== Fighting Pixel Man ====
    1. Start Game
    2. Show My Battle Status
    3. Help
    4. Quit
    """)

def introduction():
    print("Welcome to Fighting Pixel Man!")
    name = input("What should I call you? ")
    element = input("Please choose your element (Water/Fire/Earth): ").capitalize()
    while element not in ["Water", "Fire", "Earth"]:
        element = input("Please choose your element (Water/Fire/Earth): ").capitalize()
    player = Player(name, element)
    print(f"Welcome, {player.name} the {player.element} warrior!")
    return player

def initialize_pc():
    import random
    elements = ["Water", "Fire", "Earth"]
    element = random.choice(elements)
    pc = Player("PC", element)
    print(f"Your opponent is PC the {pc.element} fighter!")
    return pc

def show_help():
    print("""
    === Game Rules ===
    - Each player starts with 10 HP and 10 energy.
    - Each turn, both sides choose a move:
      1. Normal Attack       : No energy, deals 1 dmg
      2. Element Attack      : 2 energy, deals 2 dmg if you counter their element
      3. Special Attack      : 5 energy, deals 4 dmg
      4. Defend              : 2 energy, blocks 1 dmg (or 2 if you're being countered)
      5. Reflect             : 3 energy, reflects all damage back
    - Energy +1 per round.
    - Water beats Fire, Fire beats Earth, Earth beats Water.
    - Game ends when one player's HP reaches 0.
    """)

def main():
    player = introduction()

    while True:
        menu()
        try:
            option = int(input("What do you want to do? "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if option == 1:
            pc = initialize_pc()
            player.hp = 10
            player.energy = 10
            pc.hp = 10
            pc.energy = 10
            start_battle(player, pc)
        elif option == 2:
            player.show_stats()
        elif option ==3:
            with open("help.txt", "r", encoding="utf-8") as f:
                print(f.read())
        elif option == 4:
            print("Thanks for playing Fighting Pixel Man! 👋")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

