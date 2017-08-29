from classes.game import Person, bcolours
from classes.magic import Spell
from classes.inventory import Item
import random

print("\n\n")

# Create Black Magic
fire = Spell("Fire", 900, 1100, "Black")
thunder = Spell("Thunder", 1400, 1500, "Black")
blizzard = Spell("Blizzard", 2200, 2205, "Black")
meteor = Spell("Meteor", 3000, 4200, "Black")
quake = Spell("Quake", 500, 700, "Black")

# Create White Magic
cure = Spell("Cure", 750, 500, "White")
cura = Spell("Cura", 1400, 1200, "White")
curaga = Spell("Curaga", 2000, 5000, "White")

# Create some items
potion = Item("Potion", "potion", "Heals 150 HP", 150)
hipotion = Item("Hi-Potion", "potion", "Heals 340 HP", 340)
superpotion = Item("Super Potion", "potion", "Heals 1100 HP", 1100)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
megaelixir = Item("Mega Elixir", "elixir", "Fully restores HP/MP of entire party", 9999)
# Weapons
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)


player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 3}, {"item": elixir, "quantity": 5},
                {"item": megaelixir, "quantity": 5}, {"item": grenade, "quantity": 8}]

enemy_spells = [fire, curaga]


# Creating player and enemy characters and their attributes
player1 = Person("Valos", 2600, 1000, 650, 70, player_spells, player_items)  # Titan
player2 = Person("Meera", 1800, 7000, 500, 35, player_spells, player_items)  # Warlock
player3 = Person("Siv  ", 2000, 2500, 900, 50, player_spells, player_items)  # Hunter

enemy1 = Person("Ghoul  ", 14000, 2000, 500, 25, enemy_spells, [])
enemy2 = Person("Vampire", 14000, 2000, 500, 25, enemy_spells, [])
enemy3 = Person("Wraith ", 19000, 2000, 800, 100, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

# Initialisation of variables
running = True
i = 0

# Print alert message informing of enemy
print(bcolours.FAIL + bcolours.BOLD + "ENEMY ATTACKS!" + bcolours.ENDC)

# While program is running, (= True), do the stuff
while running:
    # Prints menu for user to select action
    print("======================================================")
    print("NAME                       HP                                    MP")
    for player in players:
        player.get_stats()

    print("\n")
    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        print("\n")
        print(bcolours.BOLD + bcolours.HEADER + str(player.name) + bcolours.ENDC)
        player.choose_action()
        choice = input("Choose action:")

        # Let index be choice - 1, so index corresponds to appropriate index in array
        index = int(choice) - 1

        # Print feedback message
        print("You chose", bcolours.UNDERLINE + player.action[index] + bcolours.ENDC + "!")

        # If index is first element of array (choice 1) run appropriate code
        if index == 0:
            dmg = player.generate_dmg()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_dmg(dmg)
            print(player.name.replace(" ", ""), "hit", enemies[enemy].name.replace(" ", ""), "for", dmg, "hit points!")

            if enemies[enemy].hp == 0:
                print(enemies[enemy].name.replace(" ", "") + " has died.")
                del enemies[enemy]

        # Else, if second choice, run appropriate code
        elif index == 1:
            player.choose_magic()
            choice = input("Choose spell:")
            index = int(choice) - 1
            if index == -1:
                continue

            spell = player.magic[index]
            dmg = spell.generate_damage()
            cost = spell.cost

            print("You chose " + bcolours.OKBLUE + spell.name + bcolours.ENDC + "!")

            # If player mp is less than cost, user cannot use magic, so bounce back to start of loop with 'continue'
            if player.mp < cost:
                print(bcolours.FAIL + bcolours.BOLD + "\nNot enough MP!", bcolours.ENDC)
                print("Player MP:" + bcolours.OKBLUE, player.mp, bcolours.ENDC)
                continue

            # Otherwise, reduce player mp by cost amount and proceed with program
            player.reduce_mp(cost)

            if spell.type == "White":
                player.heal(dmg)
                print(bcolours.OKBLUE + "\n" + str(spell.name), "heals for", dmg, "HP" + bcolours.ENDC)

            elif spell.type == "Black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_dmg(dmg)
                print(player.name.replace(" ", ""), "hit", enemies[enemy].name.replace(" ", ""), "for", dmg,
                      "hit points!")
                if enemies[enemy].hp == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has died.")
                    del enemies[enemy]

        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose item:")) - 1
            if item_choice == -1:
                continue
            item = player.items[item_choice]
            if player.items[item_choice]["quantity"] == 0:
                print(bcolours.FAIL + "\nNone left..." + bcolours.ENDC)
                continue
            player.items[item_choice]["quantity"] -= 1
            if item["item"].type == "potion":
                player.heal(item["item"].prop)
                print(bcolours.OKGREEN, "\n", item["item"].name, "heals for", str(item["item"].prop), "HP!",
                      bcolours.ENDC)

            elif item["item"].type == "elixir":
                if item["item"].name == "Mega Elixir":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                    print(bcolours.OKGREEN, "\n", item["item"].name, "fully restored HP and MP!", bcolours.ENDC)

            elif item["item"].type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_dmg(item["item"].prop)
                print(bcolours.FAIL, "\n" + item["item"].name, "deals", str(item["item"].prop), "damage to",
                      enemies[enemy].name.replace(" ", "") + bcolours.ENDC)
                if enemies[enemy].hp == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has died.")
                    del enemies[enemy]

        defeated_enemies = 0
        defeated_allies = 0

        for enemy in enemies:
            if enemy.hp == 0:
                defeated_enemies += 1

        for player in players:
            if player.hp == 0:
                defeated_allies += 1

        if defeated_enemies == 3:
            print(bcolours.OKGREEN + "You win!" + bcolours.ENDC)
            running = False
            if player.hp == 0:
                player.hp = 1

        elif defeated_allies == 3:
            print(bcolours.FAIL + "You lose!" + bcolours.ENDC)
            running = False

    # Enemy's turn
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)

        if enemy_choice == 0:
            target = random.randrange(0, len(players) - 1)
            print("TARGET =", target)
            enemy_dmg = enemy.generate_dmg()
            players[target].take_dmg(enemy_dmg)
            print(enemy.name.replace(" ", ""), "attacks", players[target].name.replace(" ", ""), "for", enemy_dmg,
                  "hit points!")
            if players[target].get_hp() <= 0:
                print(players[target].name.replace(" ", "") + " has died.")
                del players[target]

        if enemy_choice == 1:
            target = random.randrange(0, len(players))
            print("TARGET =", target)
            magic_choice = random.randrange(0, len(enemy.magic))
            spell = enemy.magic[magic_choice]

            if enemy.mp < spell.cost:
                continue
            else:
                enemy.reduce_mp(spell.cost)
            if spell.type == "White":
                enemy.heal(spell.dmg)
                print(bcolours.OKBLUE + str(spell.name), "heals", enemy.name.replace(" ", ""), "for", spell.dmg, "HP" +
                      bcolours.ENDC)

            elif spell.type == "Black":
                players[target].take_dmg(spell.dmg)
                print(enemy.name.replace(" ", ""), "chose", spell.name, "and dealt", spell.dmg, "damage to",
                      players[target].name.replace(" ", ""))
                if players[target].get_hp() <= 0:
                    print(players[target].name.replace(" ", "") + " has died.")
                    del players[target]

    defeated_enemies = 0
    defeated_allies = 0

    for enemy in enemies:
        if enemy.hp == 0:
            defeated_enemies += 1

    for player in players:
        if player.hp == 0:
            defeated_allies += 1

    if defeated_enemies == 3:
        print(bcolours.OKGREEN + "You win!" + bcolours.ENDC)
        running = False
        if player.hp == 0:
            player.hp = 1

    elif defeated_allies == 3:
        print(bcolours.FAIL + "You lose!" + bcolours.ENDC)
        running = False
