piano = ["d", "r", "m", "f", "s", "l", "c"]

S = input()

rabit = 2
time = 0

for score in S:
    if piano.index(score) == rabit:
        time += 1
    elif piano.index(score) > rabit:
        time += piano.index(score) - rabit + 1
        rabit = piano.index(score) 
    else:
        time += rabit - piano.index(score) + 1
        rabit = piano.index(score)

print(time)