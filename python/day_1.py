# Part 1
with open('../input/input_1.txt', 'r') as f:
    elves = {}
    calories = 0
    elf = 1
    for line in f:
        if line != '\n':
            calories += int(line)
        else:
            elves[elf] = calories
            calories = 0
            elf += 1

elves_ranked = dict(sorted(elves.items(), key=lambda item: item[1], reverse=True))
print(list(elves_ranked.values())[0])

# Part 2
print(sum(list(elves_ranked.values())[0:3]))
