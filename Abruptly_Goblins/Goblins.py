gamers = []
def add_gamer(gamer, gamers_list):
    keys = [i for i in gamer.keys()]
    if "name" in keys and 'availability' in keys:
        gamers_list.append(gamer)
    else:
        print("Wrong input")
    
kimberly = {"name": "Kimberly Warner", "availability" : ["Monday", "Tuesday", "Friday"]}
add_gamer(kimberly,gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

def build_daily_frequency_table():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    values = []
    for i in range(len(days)):
        values.append(0)
    table = { day : value for day, value in zip(days,values)}
    return table

count_availability = build_daily_frequency_table()
def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer["availability"]:
            current_value = available_frequency[day]
            updated_value = current_value + 1
            available_frequency[day] = updated_value
calculate_availability(gamers, count_availability)
#print(count_availability)
def find_best_night(availability_table):
    values = []
    for i in availability_table.values():
        values.append(i)
    values.sort()
    keys = []
    for i in availability_table.keys():
        keys.append(i)
    for key in keys:
        if availability_table[key] == values[-1]:
            return key
        else:
            continue
game_night = find_best_night(count_availability)
print(game_night)
#start after game night

        
           





