with open('input_2.txt', 'r') as f:
    score_1 = 0
    score_2 = 0
    needed_result = {'X': ('lose', 0), 'Y': ('draw', 3), 'Z': ('win', 6)}

    for line in f:
        opponent_val, me_val = line.strip().split(' ')

        # Scoring for part 1
        if (opponent_val, me_val) in [('A', 'X'), ('B', 'Y'), ('C', 'Z')]:
            score_1 += 3
        if (opponent_val, me_val) in [('A', 'Y'), ('B', 'Z'), ('C', 'X')]:
            score_1 += 6
        if me_val == 'X':
            score_1 += 1
        if me_val == 'Y':
            score_1 += 2
        if me_val == 'Z':
            score_1 += 3

        # Scoring for part 2
        score_2 += needed_result[me_val][1]
        if (opponent_val, me_val) in [('A', 'Y'), ('B', 'X'), ('C', 'Z')]:
            score_2 += 1
        if (opponent_val, me_val) in [('A', 'Z'), ('B', 'Y'), ('C', 'X')]:
            score_2 += 2
        if (opponent_val, me_val) in [('A', 'X'), ('B', 'Z'), ('C', 'Y')]:
            score_2 += 3

print(score_1)
print(score_2)
