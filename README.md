# fighting_pixel_man
A simple Python-based terminal fighting game with strategic elemental combat.
· Project Overview
Fighting Pixel Man is a turn-based pixel-style combat game where players and the PC face off using a range of elemental skills and tactics. Players choose from three classic elements—Water, Fire, and Earth—and engage in strategic battles involving attack, defense, and reflection mechanics. With a blend of ASCII art animations, simple inputs, and layered game logic.

·  Key Features
Players choose Water, Fire, or Earth as their attribute. Each element counters another (Water beats Fire, Fire beats Earth, Earth beats Water), When elemental advantage applies, element attacks deal bonus damage, and defend actions block more damage if the player is at a disadvantage.
    Water beats Fire 🔥 → 🌊
    Fire beats Earth 🌱 → 🔥
    Earth beats Water 🌊 → 🌱
Five different actions available:
(1) Normal Attack (Free, 1 dmg)
(2) Element Attack (2 energy, bonus dmg if countering)
(3) Special Attack (5 energy, high damage)
(4) Defend (2 energy, blocks 1–2 dmg)
(5) Reflect (3 energy, returns all damage received)
Each round, energy regenerates by 1, requiring players to carefully balance offense and defense. Both the player and the PC choose their actions at the same time, with outcomes based on elemental counters, defense, or reflection. Every action is brought to life with custom pixel-style ASCII animations, and all battle results—wins, losses, and draws—are tracked and viewable anytime.
