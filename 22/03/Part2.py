import string

def pop_dic():
    i=1
    dictionary = {}
    for letter in string.ascii_letters:
        dictionary[letter] = i
        i+=1
    return dictionary

prio_list = pop_dic()

bags = open("input").readlines()

prio_score = 0

while bags:
    bag1 = set(bags.pop(0).strip())
    bag2 = set(bags.pop(0).strip())
    bag3 = set(bags.pop(0).strip())

    for letter in bag1:
        if letter in bag2 and letter in bag3:
            prio_score += prio_list[letter]

print(prio_score)