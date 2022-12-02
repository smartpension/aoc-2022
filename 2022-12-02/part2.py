with open("input.txt") as input_file:
    input_values = input_file.readlines()

scores = []

for game in input_values:
    score = 0
    opponent = game[0]
    me = game[2]

    # Need to lose
    if me == "X":
        if opponent == "A":
            # Add 3 for Scissors
            score += 3
        if opponent == "B":
            # Add 1 for Rock
            score += 1
        if opponent == "C":
            # Add 2 for Paper
            score += 2
    # Need to draw
    elif me == "Y":
        if opponent == "A":
            # Add 1 for Rock
            score += 1
        if opponent == "B":
            # Add 2 for Paper
            score += 2
        if opponent == "C":
            # Add 3 for Scissors
            score += 3
        # Points for a draw
        score += 3
    if me == "Z":
        if opponent == "A":
            # Add 2 for Paper
            score += 2
        if opponent == "B":
            # Add 3 for Scissors
            score += 3
        if opponent == "C":
            # Add 1 for Rock
            score += 1
        # Points for a win
        score += 6

    scores.append(score)

print(sum(scores))
