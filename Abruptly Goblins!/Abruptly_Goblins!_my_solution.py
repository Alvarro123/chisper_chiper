#this is a solution for "Abruptly Goblins" external project in Codecademy Python 3 course, module "Dictionaries"
gamers = []
#gamer = {"name" : "Vicky Very", "availability": ["Monday", "Thursday", "Sunday"]}
def add_gamer (gamer, gamers_list):
    keys = []
    gamer = dict(gamer)
    gamers_list = list(gamers_list)
    for i in gamer.keys():
        keys.append(i)
    if "name" in keys and "availability" in keys:
        gamers_list.append(gamer["name"])
    return gamers_list

kimberly = {"name":"Kimberly Warner", "availability":["Mondays", "Tuesdays", "Fridays"]}
add_gamer(kimberly,gamers)
print("")


