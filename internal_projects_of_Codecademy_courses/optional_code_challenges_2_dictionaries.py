#PART 1
#...............................
#1. Sum values
# Write your sum_values function here:
def sum_values(my_dictionary):
    values = [i for i in my_dictionary.values()]
    sum = 0
    for i in values:
        sum+=i
    return sum
# Uncomment these function calls to test your sum_values function:
#print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
#print(sum_values({10:1, 100:2, 1000:3}))
# should print 6
#2 Even keys
# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
    even_keys = [i for i in my_dictionary.keys() if i%2 == 0]
    sum = 0
    for key in even_keys:
        sum+=my_dictionary[key]
    return sum
# Uncomment these function calls to test your  function:
#print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
#print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6
#3 Add Ten
# Write your add_ten function here:
def add_ten(my_dictionary):
    keys = [i for i in my_dictionary.keys()]
    values = [(i + 10) for i in my_dictionary.values()]
    return {key:value for key, value in zip(keys,values)}
# Uncomment these function calls to test your  function:
#print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
#print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}
#4 Values that are keys
# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
    list_of_keys = [i for i in my_dictionary.keys()]
    list_of_values = [i for i in my_dictionary.values()]
    values_that_are_keys_list = []
    for value in list_of_values:
        if value in list_of_keys:
            values_that_are_keys_list.append(value)
        else:
            continue
    return values_that_are_keys_list
# Uncomment these function calls to test your  function:
#print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
#print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]
#5. Largest Value
# Write your max_key function here:
def max_key(my_dictionary):
    list_of_valu = [i for i in my_dictionary.values()]
    list_of_valu.sort()
    max_value = 0
    for i in list_of_valu[-1:]:
        max_value += i
    for key in my_dictionary.keys():
        if my_dictionary[key] == max_value:
            return key
        else:
            continue
# Uncomment these function calls to test your  function:
#print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
#print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"
#PART 2
#.........................................................
#1.Word Lenght Dict
# Write your word_length_dictionary function here:
def word_length_dictionary(words):
    list_of_lenghts = []
    for word in words:
        list_of_lenghts.append(len(word))
    return {w:l for w,l in zip(words,list_of_lenghts)}

# Uncomment these function calls to test your  function:
#print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
#print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}
#2. Frequency Count
# Write your frequency_dictionary function here:
def frequency_dictionary(words):
    counts = []
    for word in words:
        counts.append(words.count(word))
    return {w:c for w,c in zip(words,counts)}

# Uncomment these function calls to test your  function:
#print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
#print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}
#3. Unique Values
# Write your unique_values function here:
def unique_values(my_dictionary):
    val = [i for i in my_dictionary.values()]
    val_c = []
    for v in val:
        val_c.append(val.count(v))
    dic = {va:c for va, c in zip(val,val_c)}
    return len([i for i in dic.keys()])

# Uncomment these function calls to test your  function:
#print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
#print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1
#4. Count first letter
# Write your count_first_letter function here:
def count_first_letter(names):
    last_names = [i for i in names.keys()]
    list_of_first_letters = []
    for last in last_names:
        list_of_first_letters.append(last[0])
    cout_of_people_of_first_letter = [len(i) for i in names.values()]
    letters_more_than_one = []
    values_for_letters_more_than_one = []
    letters_only_one = []
    values_for_letters_only_one = []
    for l in list_of_first_letters:
        if list_of_first_letters.count(l) > 1:
            letters_more_than_one.append(l)
        else:
            letters_only_one.append(l)
    for i in letters_only_one:
        values_for_letters_only_one.append(cout_of_people_of_first_letter[list_of_first_letters.index(i)])
    for x in list_of_first_letters:
        if x in letters_only_one:
            cout_of_people_of_first_letter.remove(cout_of_people_of_first_letter[list_of_first_letters.index(x)])
            list_of_first_letters.remove(x)
        else:
            continue
    k = []
    for t in list_of_first_letters:
        if t in k:
            continue
        else:
            k.append(t)
    vk = []
    while len(vk) < len(k):
        vk.append(0)
    for q in range(len(list_of_first_letters)):
        for a in k:
            if list_of_first_letters[q] == a:
                vk[k.index(a)] += cout_of_people_of_first_letter[q]
            else:
                continue
    dic1 = {z:c for z,c in zip(k,vk)}
    dic2 = {s:b for s,b in zip(letters_only_one,values_for_letters_only_one)}
    dic3 = {}
    dic3.update(dic1.items())
    dic3.update(dic2.items())
    return dic3

# Uncomment these function calls to test your  function:
#print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
#print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
