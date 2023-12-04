with open("pokemon_list/common_list.txt") as f:
    common = [word for line in f for word in line.split()]
with open("pokemon_list/uncommon_list.txt") as f:
    uncommon = [word for line in f for word in line.split()]
with open("pokemon_list/rare_list.txt") as f:
    rare = [word for line in f for word in line.split()]
with open("pokemon_list/legendary_list.txt") as f:
    legendary = [word for line in f for word in line.split()]
with open("item_list/berry_list.txt") as f:
    berry = [word+" Berry" for line in f for word in line.split()]
with open("item_list/ball_list.txt") as f:
    ball = [word+" Ball" for line in f for word in line.split()]
# with open("pokemon_list/thunderwave_list") as f:
#     thunderwave = [word for line in f for word in line.split()]
# with open("pokemon_list/hypnosis_list") as f:
#     hypnosis = [word for line in f for word in line.split()]

common_list = {}
uncommon_list = {}
rare_list = {}
legendary_list = {}

item_list = {}

ball_list = {}

# thunderwave_list = {}
# hypnosis_list = {}

item = ball + berry

i = 1
a = 0
while i < len(item) + 1:
    item_list[i] = item[a]
    i += 1
    a += 1

bi = 1
ba = 0
while bi < len(ball) + 1:
    ball_list[bi] = ball[ba]
    bi += 1
    ba += 1

ci = 1
ca = 0
while ci < len(common) + 1:
    common_list[ci] = common[ca]
    ci += 1
    ca += 1

ui = 1
ua = 0
while ui < len(uncommon) + 1:
    uncommon_list[ui] = uncommon[ua]
    ui += 1
    ua += 1

ri = 1
ra = 0
while ri < len(rare) + 1:
    rare_list[ri] = rare[ra]
    ri += 1
    ra += 1

li = 1
la = 0
while li < len(legendary) + 1:
    legendary_list[li] = legendary[la]
    li += 1
    la += 1

# ti = 1
# ta = 0
# while ti < len(thunderwave) + 1:
#     thunderwave_list[ti] = thunderwave[ta]
#     ti += 1
#     ta += 1
#
# hi = 1
# ha = 0
# while hi < len(hypnosis) + 1:
#     hypnosis_list[hi] = hypnosis[ha]
#     hi += 1
#     ha += 1
#
# fightable = hypnosis + thunderwave

amount_item = len(item_list)
amount_ball = len(ball_list)
amount_common = len(common_list)
amount_uncommon = len(uncommon_list)
amount_rare = len(rare_list)
amount_legendary = len(legendary_list)

# print(ball)
# print(item)
# print(amount_item)
# print(common_list)
# print(uncommon_list)
# print(rare_list)
# print(legendary_list)
# print(item_list)
# print(ball_list)
# print(item[0])
# print(hypnosis)
# print(hypnosis_list)


starter_list = {
    1: "Bulbasaur",
    2: "Squirtle",
    3: "Charmander",
}

item_list = {

}

dialogue1 = ["Hello there!",
             "Welcome to the world of Pokémon!",
             "My name is Oak!",
             "People call me the Pokémon Prof!",
             "This world is inhabited by creatures called Pokémon!",
             "For some people, Pokémon are pets",
             "Other use them for fights",
             "Myself… I study Pokémon as a profession",
             "First, what is your name?",
             ]



dialogue_getpokemon1 = ["Hey!",
                        "Wait!",
                        "Don't go out!",
                        "It's unsafe!",
                        "Wild Pokémon live in tall grass!",
                        "You need your own Pokémon for your protection",
                        "I know!",
                        "Here",
                        "Come with me!",
                        ]

