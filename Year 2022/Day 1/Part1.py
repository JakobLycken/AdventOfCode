

elves_carry = open("input")

current_calories = 0
max_calories = 0

for line in elves_carry:
    calories = line
    if calories == "\n":
        if current_calories > max_calories:
            max_calories = current_calories
        current_calories = 0
    else:
        current_calories += int(calories)

print(max_calories)