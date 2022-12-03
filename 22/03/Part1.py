import string

def pop_dic():
    i=1
    dictionary = {}
    for letter in string.ascii_letters:
        dictionary[letter] = i
        i+=1
    return dictionary

prio_list = pop_dic()
print(prio_list)
bags = open("input")

prio_score = 0
for bag in bags:
    bag = bag.strip()
    half = int(len(bag)/2)
    bag1 = set(bag[0:half])
    bag2 = set(bag[half:])
    for letter in bag1:
        if letter in bag2:
            prio_score += prio_list[letter]
            break

print(prio_score)