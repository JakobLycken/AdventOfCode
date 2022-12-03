elves_carry = open("input")

current_calories = 0
max_calories = [0, 0, 0]

for calories in elves_carry:
    if calories == "\n":
        for i in range(3):
            if current_calories > max_calories[i]:
                max_calories.insert(i,current_calories)
                max_calories.pop(3)
                break
        current_calories = 0
    else: current_calories += int(calories)

print(max_calories)
print(sum(max_calories))
