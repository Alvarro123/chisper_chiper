
def decode_vinegre(message,keyword):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    message = str(message)
    message = message.lower()
    keyword = str(keyword)
    keyword = keyword.lower()
    keyword_indexes = []
    letter_indexes = []
    special_character_indexes = []
    special_character_list = []
    spaces_indexes = []
    spaces_list = []
    coded_list = []
    keyword_list = []
    decoded_list = []
    output = []
    for i in keyword:
        keyword_indexes.append(alphabet.index(i))
    for i in range(len(message)):
        if alphabet.count(message[i]) > 0:
            letter_indexes.append(i)
        elif message[i] == " ":
            spaces_list.append(message[i])
            spaces_indexes.append(i)
        else:
            special_character_list.append(message[i])
            special_character_indexes.append(i)
    for i in letter_indexes:
        coded_list.append(alphabet.index(message[i]))
    
    while len(keyword_list) < len(letter_indexes):
        for key in keyword_indexes:
            keyword_list.append(key)
    for i in range(len(letter_indexes)):
        decoded_index = (coded_list[i] - len(alphabet)) + keyword_list[i]
        decoded_list.append(alphabet[decoded_index])
    decoded_letters = list(zip(letter_indexes,decoded_list))
    decoded_spaces = list(zip(spaces_indexes,spaces_list))
    decoded_special_characters = list(zip(special_character_indexes, special_character_list))
    complete_list = decoded_letters + decoded_spaces + decoded_special_characters
    complete_list.sort()
    for i in range(len(message)):
        output.append(complete_list[i][1])

    return ''.join(output)




