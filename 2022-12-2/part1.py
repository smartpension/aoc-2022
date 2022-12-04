with open("input.txt") as input_file:
    input_values = input_file.readlines()

scores = []

for game in input_values:
    score = 0
    opponent = game[0]
    me = game[2]

    if me == "X":
        if opponent == "A":
            score += 3
        if opponent == "C":
            score += 6
        score += 1
    elif me == "Y":
        if opponent == "A":
            score += 6
        if opponent == "B":
            score += 3
        score += 2
    if me == "Z":
        if opponent == "B":
            score += 6
        if opponent == "C":
            score += 3
        score += 3

    scores.append(score)

print(sum(scores))
