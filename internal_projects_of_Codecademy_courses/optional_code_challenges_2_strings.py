#PART 1
#
# 1. Unique letters
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
    word = str(word)
    list_of_letters = []
    number_of_letters = []
    for letter in word:
        number_of_letters.append(word.count(letter))
        list_of_letters.append(letter)
    word_dict = { let : count for let, count in zip(list_of_letters, number_of_letters)}
    return len(list(word_dict))     
# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
#.............................................
#2. Count X
# Write your count_char_x function here:
def count_char_x(word, x):
    word = str(word)
    x = str(x)
    if x in word:
        return word.count(x)
    else:
        return "This letter does NOT appear in given word !"
        
# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1
#.............................................
#3. Count multiple X
# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
    word = str(word)
    x = str(x)
    new_word = word.split(x)
    new_word = "".join(new_word)
    number_of_occurances = int((len(word) - len(new_word))/(len(x)))
    return number_of_occurances

# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1
#.............................................
#4. Substring Between
#Write your substring_between_letters function here:
def substring_between_letters(word,start,end):
    word = str(word)
    start = str(start)
    end = str(end)
    if word.find(start) == -1 or word.find(end) == -1:
        return word
    else:
        start_index = word.find(start) + 1
        end_index = word.find(end)
        return word[start_index:end_index]
    
# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"
#.............................................
#5. X-lengths
#Write your x_length_words function here:
def x_length_words(sentence,x):
    sentence = str(sentence)
    x = int(x)
    list_of_words = sentence.split(" ")
    for word in list_of_words:
        if len(word) >= x:
            continue
        else:
            return False
    return True           
# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True
#PART 2 
#
#1. Check Name
# Write your check_for_name function here:
def check_for_name(sentence,name):
    sentence = str(sentence)
    name = str(name)
    sentence = sentence.lower()
    name = name.lower()
    sentence = sentence.split(" ")
    list_of_lengths = []
    for word in sentence:
        list_of_lengths.append(len(word))
    if len(name) in list_of_lengths:
        dit_len = {len : w for len, w in zip(list_of_lengths,sentence)}
    else:
        return False
    if dit_len[len(name)] == name:
        return True
    else:
        return False

# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False
#2. Every other letter
# Write your every_other_letter function here:
def every_other_letter(word):
    new_string = ""
    index = 0
    while index <= (len(word) - 1):
        new_string += word[index]
        index += 2
    return new_string
# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 
#3.Reverse
# Write your reverse_string function here:
def reverse_string(string):
    string = str(string)
    new_string = []
    list_indexes_current_string = [i for i in range(len(string))]
    list_indexes_current_string.reverse()
    for index in list_indexes_current_string:
        new_string.append(string[index])
    return "".join(new_string)
   
# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print
#4. Make a Spoonierism
# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
    word1 = str(word1)
    word2 = str(word2)
    list_word_1 = []
    list_word_2 = []
    for letter in word1:
        list_word_1.append(letter)
    for letter in word2:
        list_word_2.append(letter)
    add1 = list_word_2[0]
    add2 = list_word_1[0]
    list_word_1[0] = add1
    list_word_2[0] = add2
    word1 = str(''.join(list_word_1)) 
    word2 = str(''.join(list_word_2))
    return word1 +" "+ word2

# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a
#5. Exclamation
# Write your add_exclamation function here:
def add_exclamation(word):
    word = str(word)
    if len(word) < 20:
        while len(word) < 20:
            word += "!"
        return word
    else:
        return word
# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn