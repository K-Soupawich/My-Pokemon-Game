import os
import time
import random
from settings import *

PC = []
#Bag = ["Poke Ball", "Poke Ball", "Poke Ball", "Poke Ball", "Poke Ball", "Great Ball", "Great Ball", "Great Ball", "Ultra Ball"]
Bag = ["Ultra Ball", "Ultra Ball", "Ultra Ball", "Ultra Ball", "Ultra Ball", "Ultra Ball", "Ultra Ball", "Ultra Ball", "Ultra Ball", "Poke Ball", "Poke Ball", "Poke Ball", "Poke Ball", "Poke Ball", "Poke Ball", "Poke Ball", "Poke Ball", "Poke Ball", "Poke Ball", "Poke Ball"]

count = 0

catch_count = 0


def looping(waittime, speed, x):
    timer = float(waittime)
    dot = [" ", ".", "..", "..."]

    while True:
        for i in dot:
            print(x + i, end="")
            print("\r" + x + i, end="")
            time.sleep(0.75)
            timer -= float(speed)
        if timer <= 0:
            break


def start():
    for x in dialogue1:
        print(x)
        time.sleep(1.5)
    time.sleep(1)

    def enter_name():
        global name
        name = str(input("> "))
        time.sleep(1)
        print("Is it " + name + "? Did I heard that right? (Y/N)")
        time.sleep(1)
        while True:
            confirm = str(input("> ").upper())
            if confirm == "Y" or confirm == "YES":
                return name
                time.sleep(0.75)
                os.system("cls")
            elif confirm == "N" or confirm == "NO":
                time.sleep(0.5)
                print("So, What is your name?")
                time.sleep(1)
                enter_name()
            continue

    enter_name()
    time.sleep(0.5)
    dialogue2 = ["Right!",
                 "So your name is " + name,
                 name + "! Your very own Pokémon legend is about to unfold!",
                 "A world of dreams and adventures with Pokémon awaits!",
                 "Let's go!"
                 ]
    for y in dialogue2:
        print(y)
        time.sleep(1.5)

    time.sleep(3.5)
    os.system("cls")

    def prologue_choice():
        global count
        print("Pokemon")
        print("1 : Enter Tall Grass\n2 : Open PC\n3 : Open Bag")
        menu_choice = str(input("> "))
        time.sleep(0.35)
        os.system("cls")
        if menu_choice == "1":
            looping(1.5, 0.5, "Entering Tall Grass")
            print("\n")
            time.sleep(0.75)
            os.system("cls")
            for z in dialogue_getpokemon1:
                print("Prof. Oak : " + z)
                time.sleep(1.5)
            time.sleep(2)
            print("===================")
            print("At Prof. Oak's Lab")
            time.sleep(1.5)
            dialogue_getpokemon2 = ["Here, " + name + " There are 3 Pokémon here!",
                                    "Haha!",
                                    "They are inside the Poké Balls",
                                    "When I was young",
                                    "I was a serious Pokémon trainer!",
                                    "In my old age, I have only 3 left",
                                    "But you can have one!",
                                    "Choose!"
                                    ]
            for i in dialogue_getpokemon2:
                print("Prof. Oak : " + i)
                time.sleep(1.5)

            def get_first_pokemon():
                print("Prof. Oak : Now " + name + " which Pokémon do you want?")
                print("1 : Bulbasaur\n2 : Squirtle\n3 : Charmander")
                first_pokemon = str(input("> "))
                time.sleep(0.25)
                if first_pokemon.isnumeric():
                    if first_pokemon == "1" or first_pokemon == "2" or first_pokemon == "3":
                        first_pokemon = int(first_pokemon)
                        print("So you want", starter_list[first_pokemon], "(Y/N)")
                        pass
                    else:
                        print("Prof. Oak : There're only 3 Poké Balls!")
                        time.sleep(1.5)
                        os.system("cls")
                        get_first_pokemon()
                    while True:
                        confirm = str(input("> ").upper())
                        if confirm == "Y" or confirm == "YES":
                            time.sleep(0.25)
                            print("You chose", starter_list[first_pokemon], "!")
                            time.sleep(1)
                            PC.append(starter_list[first_pokemon])
                            print(starter_list[first_pokemon], "was sent to Your PC")
                            time.sleep(3)
                            os.system("cls")
                            break
                        elif confirm == "N" or confirm == "NO":
                            time.sleep(0.5)
                            os.system("cls")
                            get_first_pokemon()
                            continue
                else:
                    if first_pokemon.isdecimal() == False:
                        time.sleep(0.5)
                        print(f"Prof. Oak : {first_pokemon}? What do you mean?")
                        time.sleep(2.5)
                        print("Prof. Oak : Never mind. Let's continue!")
                        time.sleep(2)
                        print("Prof. Oak : Choose one of the three Pokémon!")
                        time.sleep(4)
                        os.system("cls")
                        get_first_pokemon()

                def dialogue_after_get_pokemon():
                    dialogue_after = ["Now!",
                                      "You've chosen your first Pokémon",
                                      "It's time for you to go out and explore the world!",
                                      "We shall meet again soon " + name + "!",
                                      "Good luck!",
                                      ]
                    for a in dialogue_after:
                        print("Prof. Oak : " + a)
                        time.sleep(1.5)

                dialogue_after_get_pokemon()

            time.sleep(1)
            get_first_pokemon()
        elif menu_choice == "2":
            count += 1
            print("The PC can't seems to turn on")
            time.sleep(1.5)
            if count > 3:
                print(name + ": I should start exploring")
                time.sleep(2.5)
            os.system("cls")
            prologue_choice()

        elif menu_choice == "3":
            count += 1
            print("Your Bag is empty")
            time.sleep(1.5)
            # print(count)
            if count > 3:
                print("\"I should start exploring\"")
                time.sleep(2.5)
            os.system("cls")
            prologue_choice()

        else:
            print("That wasn't in option!")
            time.sleep(1.5)
            os.system("cls")
            prologue_choice()

    prologue_choice()


start()
time.sleep(5)
os.system("cls")


def explore():
    global ball_bag, ballchoice, item_chance
    ball_bag = []
    ballchoice = ""
    pokemonmenu = []

    os.system("cls")
    item_drop_chance = (1, 10)
    item_chance = random.randint(1, amount_item)
    shiny_chance = random.randint(1, 100)
    rarity = random.randint(1, 100)
    if rarity <= 50:
        pokemon = random.randint(1, amount_common)
        pokemon_list = common_list

    elif rarity > 50 or rarity <= 80:
        pokemon = random.randint(1, amount_uncommon)
        pokemon_list = uncommon_list

    elif rarity > 80 or rarity <= 97:
        pokemon = random.randint(1, amount_rare)
        pokemon_list = rare_list

    else:
        pokemon = random.randint(1, amount_legendary)
        pokemon_list = legendary_list

    time.sleep(0.5)
    encountertime = round(random.uniform(0.25, 3), 1)
    looping(encountertime, 0.25, "Entering Tall Grass")
    time.sleep(0.25)
    os.system("cls")
    time.sleep(0.25)
    print("\nWild", pokemon_list[pokemon], "appear!")
    if shiny_chance >= 90:
        time.sleep(0.5)
        print("Its color seems to be different")
        is_shiny = True
    if item_drop_chance == 10:
        time.sleep(0.5)
        print("Looks like it's holding something")

    def action():
        global catch_count, ballchoice, cmax, cmin, f1max, f1min, f2max, f2min, f3max, f3min, f4max, f4min
        cmin, cmax = 0, 0
        f4min, f4max = 0, 0
        f3min, f3max = 0, 0
        f2min, f2max = 0, 0
        f1min, f1max = 0, 0

        seen_ballbag_list = {}
        seen_pkm_list = {}

        print("What will you do?")
        time.sleep(0.5)
        print("1 : Bag\n2 : Run")
        choice_action = str(input("> "))
        if choice_action == "1":
            def openbag():
                global ball_bag, ballchoice
                seen_ballbag = set()
                seen_ballbag_list = {}
                i = 1
                a = 0
                for item in Bag:
                    if item in ball:
                        ball_bag.append(item)
                seen_ballbag = set(ball_bag)
                seen_ballbag = tuple(seen_ballbag)
                while i < len(seen_ballbag) + 1:
                    seen_ballbag_list[i] = seen_ballbag[a]
                    i += 1
                    a += 1
                print("Black's Bag")
                j = 1

                for keys, values in seen_ballbag_list.items():
                    for item in ball_bag:
                        if item == values and item != "Beast Ball":
                            if keys == j:
                                print(f"{keys} : {values} (x{ball_bag.count(item)})")
                                j += 1
                choice = str(input("> ").upper())
                if choice == "B":
                    time.sleep(0.25)
                    os.system("cls")
                    action()
                else:
                    pass
                if choice.isnumeric():
                    choice = int(choice)
                    for keys in seen_ballbag_list.keys():
                        if choice == keys:
                            global cmax, cmin, f1max, f1min, f2max, f2min, f3max, f3min, f4max, f4min
                            if seen_ballbag_list[choice] == "Poke Ball" or seen_ballbag_list[choice] == "Luxury Ball":
                                Bag.remove("Poke Ball")
                                if rarity <= 50:
                                    cmin, cmax = 1, 44  # 1-44
                                    f4min, f4max = 45, 73  # 45-73
                                    f3min, f3max = 74, 90  # 74-90
                                    f2min, f2max = 91, 98  # 91-98
                                    f1min, f1max = 99, 100  # 99-100
                                elif rarity > 50 or rarity <= 80:
                                    cmin, cmax = 1, 34  # 1-34
                                    f4min, f4max = 35, 64  # 35-64
                                    f3min, f3max = 65, 80  # 65-80
                                    f2min, f2max = 81, 92  # 81-92
                                    f1min, f1max = 93, 100  # 93-100
                                elif rarity > 80 or rarity <= 97:
                                    cmin, cmax = 1, 19  # 1-19
                                    f4min, f4max = 20, 32  # 20-32
                                    f3min, f3max = 33, 50  # 33-50
                                    f2min, f2max = 51, 72  # 51-72
                                    f1min, f1max = 73, 100  # 73-100
                                else:
                                    cmin, cmax = 1, 6  # 1-6
                                    f4min, f4max = 7, 11  # 7-11
                                    f3min, f3max = 12, 14  # 12-14
                                    f2min, f2max = 15, 16  # 15-16
                                    f1min, f1max = 17, 100  # 17-100
                                ballchoice = "Poke Ball"
                            elif seen_ballbag_list[choice] == "Great Ball":
                                Bag.remove("Great Ball")
                                if rarity <= 50:
                                    cmin, cmax = 1, 64
                                    f4min, f4max = 65, 84
                                    f3min, f3max = 85, 94
                                    f2min, f2max = 95, 100
                                    f1min, f1max = 101, 102
                                elif rarity > 50 or rarity <= 80:
                                    cmin, cmax = 1, 49
                                    f4min, f4max = 50, 72
                                    f3min, f3max = 73, 88
                                    f2min, f2max = 89, 96
                                    f1min, f1max = 97, 100
                                elif rarity > 80 or rarity <= 97:
                                    cmin, cmax = 1, 34
                                    f4min, f4max = 35, 58
                                    f3min, f3max = 59, 74
                                    f2min, f2max = 75, 89
                                    f1min, f1max = 89, 100
                                else:
                                    cmin, cmax = 1, 14
                                    f4min, f4max = 15, 22
                                    f3min, f3max = 23, 29
                                    f2min, f2max = 30, 34
                                    f1min, f1max = 35, 100
                                ballchoice = "Great Ball"
                            elif seen_ballbag_list[choice] == "Ultra Ball":
                                Bag.remove("Ultra Ball")
                                if rarity <= 50:
                                    cmin, cmax = 1, 89
                                    f4min, f4max = 90, 96
                                    f3min, f3max = 97, 100
                                    f2min, f2max = 101, 102
                                    f1min, f1max = 103, 104
                                elif rarity > 50 or rarity <= 80:
                                    cmin, cmax = 1, 79
                                    f4min, f4max = 80, 89
                                    f3min, f3max = 90, 96
                                    f2min, f2max = 97, 100
                                    f1min, f1max = 101, 102
                                elif rarity > 80 or rarity <= 97:
                                    cmin, cmax = 1, 69
                                    f4min, f4max = 70, 86
                                    f3min, f3max = 87, 94
                                    f2min, f2max = 95, 98
                                    f1min, f1max = 99, 100
                                else:
                                    cmin, cmax = 1, 34
                                    f4min, f4max = 35, 64
                                    f3min, f3max = 65, 85
                                    f2min, f2max = 86, 97
                                    f1min, f1max = 98, 100
                                ballchoice = "Ultra Ball"
                            elif seen_ballbag_list[choice] == "Master Ball":
                                Bag.remove("Master Ball")
                                cmin, cmax = 1, 100
                                f4min, f4max = 101, 102
                                f3min, f3max = 103, 104
                                f2min, f2max = 105, 106
                                f1min, f1max = 107, 108
                                ballchoice = "Master Ball"
                            else:
                                continue
                        else:
                            continue

                else:
                    print("That not exist!")
                    time.sleep(1.5)
                    os.system("cls")
                    openbag()
                ball_bag = []

            openbag()
            # print(seen_ballbag_list)
            catch_chance = random.randint(1, 100)
            print("You throw " + ballchoice + "!")

            def item_dropped():
                global item_chance
                time.sleep(1)
                print("The wild", pokemon_list[pokemon], "dropped", item[item_chance])
                time.sleep(0.75)
                print("You put", item[item_chance], "in your bag")
                Bag.append(item[item_chance])

            if f1max >= catch_chance >= f1min:
                catch_count += 1
                time.sleep(1)
                print("Poké Ball doesn't shake")
                time.sleep(1)
                print("Poké Ball broke!")
                time.sleep(0.75)
                print("Oh no! The", pokemon_list[pokemon], "broke free!")
            elif f2max >= catch_chance >= f2min:
                catch_count += 1
                time.sleep(1)
                print("Poké Ball shake 1 time")
                time.sleep(1)
                print("Poké Ball broke!")
                time.sleep(0.75)
                print("Darn! The", pokemon_list[pokemon], "broke free!")
            elif f3max >= catch_chance >= f3min:
                catch_count += 1
                time.sleep(1)
                print("Poké Ball shake 2 time")
                time.sleep(1)
                print("Poké Ball broke!")
                time.sleep(0.75)
                print("Aargh! Almost had it!")
            elif f4max >= catch_chance >= f4min:
                catch_count += 1
                time.sleep(1)
                print("Poké Ball shake 3 time")
                time.sleep(1)
                print("Poké Ball broke!")
                time.sleep(0.75)
                print("Shoot! It was so close, too!")
            elif cmax >= catch_chance >= cmin:
                time.sleep(1)
                print("Poké Ball shake 3 time")
                if is_shiny:
                    time.sleep(1)
                    print("Gotcha! ✨", pokemon_list[pokemon], "was caught!")
                    if item_drop_chance == 10:
                        time.sleep(1)
                        item_dropped()
                    time.sleep(1.5)
                    print(pokemon_list[pokemon], "was sent to PC!")
                    PC.append("✨" + pokemon_list[pokemon])
                else:
                    time.sleep(1)
                    print("Gotcha!", pokemon_list[pokemon], "was caught!")
                    if item_drop_chance == 10:
                        time.sleep(1)
                        item_dropped()
                    time.sleep(1.5)
                    print(pokemon_list[pokemon], "was sent to PC!")
                    PC.append(pokemon_list[pokemon])
                time.sleep(1)
                os.system("cls")
                mainmenu()
            if catch_count == 5:
                time.sleep(1.5)
                print("Wild", pokemon_list[pokemon], "fled!")
                time.sleep(2)
                mainmenu()
            print("catch count :"+str(catch_count))
            time.sleep(1.5)
            os.system("cls")
            action()

        elif choice_action == "2":
            time.sleep(0.25)
            print("You ran away!")
            time.sleep(2)
            os.system("cls")
            mainmenu()
        else:
            print("That wasn't in option!")
            time.sleep(1.5)
            os.system("cls")
            action()

    action()


def open_pc():
    os.system("cls")
    seen_PC = set(PC)
    print(name + "'s PC")
    print("==============")
    for pokemon in seen_PC:
        print(f"-{pokemon} (x{PC.count(pokemon)})")
    while True:
        back = str(input("> ").upper())
        if back == "B":
            time.sleep(0.25)
            os.system("cls")
            mainmenu()
        continue


def open_bag():
    os.system("cls")
    seen_Bag = set(Bag)
    print("Your Bag")
    print("==============")
    for item in seen_Bag:
        print(f"-{item} (x{Bag.count(item)})")
    while True:
        back = str(input("> ").upper())
        if back == "B":
            time.sleep(0.25)
            os.system("cls")
            mainmenu()
        continue


def mainmenu():
    print("Pokemon")
    time.sleep(0.5)
    print("1 : Explore\n2 : Open PC\n3 : Open Bag")
    menu_choice = str(input("> "))
    if menu_choice == "1":
        explore()
    elif menu_choice == "2":
        open_pc()
    elif menu_choice == "3":
        open_bag()
    else:
        print("That wasn't in option!")
        time.sleep(1.5)
        os.system("cls")
        mainmenu()


mainmenu()