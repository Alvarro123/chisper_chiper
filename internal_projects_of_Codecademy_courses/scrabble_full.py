# This is a solution for internal project "Scrabble" i Dictionaries module of Python 3 course
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letter_to_points = {key : value for key, value in zip(letters, points)}
letter_to_points.update({" " : 0})
def score_word(word):
    word = str(word)
    word = word.upper()
    point_total = 0
    for letter in word:
        if letter in letter_to_points:
            point_total += letter_to_points[letter]
        else:
            point_total+=0
    return point_total
#brownie_points = score_word("BROWNIE")
#print(brownie_points)
player_to_words = { "player1": ["BLUE","TENNIS", "EXIT"], "wordNerd" : ["EARTH", "EYES", "MACHINE"], "LexiCon":["ERASER", "BELLY", "HUSKY"], "ProfReader" : ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}
for player in player_to_words.keys():
    player_points = 0
    for word in player_to_words[player]:
        player_points += score_word(word)
    player_to_points.update({player : player_points})
#print(player_to_points)
#FUNCTION play_word() : take in a player and a word, and add the word to the list of words they've played
def play_word(player,word):
    words = player_to_words[player]
    player_to_words.pop(player)
    words += [word]
    add = {player : words}
    player_to_words.update(add)
    return player_to_words

#player1 = "player1"
#word = "MAMA"
#print(play_word(player1, word))
 
#update_point_totals() — turn your nested loops into a function that you can call any time a word is played
def update_point_totals(player,word):
    play_word(player,word)
    player_to_points = {}
    for player in player_to_words.keys():
        player_points = 0
        for word in player_to_words[player]:
            player_points += score_word(word)
        player_to_points.update({player : player_points})
    return player_to_points

player = "wordNerd"
word = "lesiu"
print(update_point_totals(player,word))

#make your letter_to_points dictionary able to handle lowercase inputs as well
#DONE

