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
    days_keys = list(available_frequency.keys())
    spots_values = list(available_frequency.values())
    #print(days_keys)
    #print(spots_values)
    for gamer in gamers_list:
            for day in list(gamer["availability"]):
                index = days_keys.index(day)
                spots_values[index] +=1
    return {k : d for k, d in zip(days_keys,spots_values)}

count_availability = calculate_availability(gamers, count_availability)
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
#print(game_night)
def available_on_night(gamers_list, day):
    available_people = []
    for gamer in gamers_list:
        if day in gamer["availability"]:
            available_people.append(gamer["name"])
        else:
            continue
    return available_people

attending_game_night = available_on_night(gamers,game_night)
#print(attending_game_night)
form_email = "Hi, {name}, {game} session will be played in {day}."
def send_email(form_email,available_gamers,day,game):
    for gamer in available_gamers:
        form_email = str(form_email)
        name = str(gamer)
        game = str(game)
        day = str(day)
        print(form_email.format(name=name, game=game, day=day))
game = "Abruptly Goblins!"
#send_email(form_email,attending_game_night,game_night,game)
#print(attending_game_night)
#print(gamers)
def unable_to_attend(gamers_list, able_to_attend):
    unable_to_attend = []
    for i in gamers_list:
        name = list(i["name"])
        name_join = ''.join(name)
        #print(name_join)
        if name_join in able_to_attend:
                continue
        else:
            unable_to_attend.append(i)
    return unable_to_attend
unable_to_attend_best_night = unable_to_attend(gamers, attending_game_night)
second_night_availability = build_daily_frequency_table()
second_night_availability = calculate_availability(unable_to_attend_best_night,second_night_availability)
#print(second_night_availability)
second_night = find_best_night(second_night_availability)
#print(second_night)
available_second_game_night = available_on_night(gamers,second_night)
#print(available_second_game_night)
send_email(form_email,available_second_game_night,second_night,game)
#DONE - ENTIRE PROJECT COMPLETED
    


        
           





