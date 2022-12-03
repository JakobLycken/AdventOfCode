strat = open("input")

score = {"win" : 6, "draw" : 3, "loss" : 0}
outcome = {"X" : "loss", "Y":"draw", "Z":"win"}
outcome = {"X" : [{"A" : "scissor", "B" : "rock", "C" : "paper"},0],
           "Y" : [{"A" : "rock", "B" : "paper","C" : "scissor"},3],
           "Z" : [{"A" : "paper", "B" : "scissor", "C" : "rock"},6]
           }

win = {"A": "paper", "B": "scissor", "C":"rock"}
loss = {"A": "scissor", "B":"rock", "C":"paper"}
draw = {"A": "rock", "B":"paper","C":"scissor"}

hand = {"rock" :1, "paper":2, "scissor":3}

current_score = 0

for play in strat:
    play = play.strip("\n")
    current_score += outcome[play[2]][1] + hand[outcome[play[2]][0][play[0]]]

print(current_score)