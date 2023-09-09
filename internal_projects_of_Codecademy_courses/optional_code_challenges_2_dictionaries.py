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
####### START FROM PART 2!!!!