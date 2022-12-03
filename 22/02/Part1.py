strat = open("input")

score = {"win" : 6, "draw" : 3, "loss" : 0}
outcome = {"A X" : "draw", "A Y":"win", "A Z":"loss",
           "B X":"loss", "B Y": "draw", "B Z":"win",
           "C X":"win", "C Y":"loss", "C Z":"draw"}
hand = {"X" :1, "Y":2, "Z":3}

current_score = 0

for play in strat:
    play = play.strip("\n")
    current_score += score[outcome[play]] + hand[play[2]]

print(current_score)