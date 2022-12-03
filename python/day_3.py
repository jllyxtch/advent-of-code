# Part 1
with open('input/input_3.txt', 'r') as f:
    priority_sum = 0

    for line in f:
        half = int(len(line.strip())/2)
        first_compartment = set(line.strip()[:half])
        second_compartment = set(line.strip()[half:])

        doubled_item = list(first_compartment.intersection(second_compartment))[0]
        priority = ord(
            doubled_item) - 38 if doubled_item.isupper() else ord(doubled_item) - 96
        priority_sum += priority

print(priority_sum)

# Part 2
with open('input/input_3.txt', 'r') as f:
    priority_sum = 0
    lines = f.readlines()
    groups = [lines[i * 3:(i + 1) * 3] for i in range((len(lines) + 2) // 3)]

    for group in groups:
        group_sets = [set(member) for member in group]
        badge = list(group_sets[0].intersection(
            group_sets[1]).intersection(group_sets[2]))
        if '\n' in badge:
            badge.remove('\n')
        priority = ord(badge[0]) - 38 if badge[0].isupper() else ord(badge[0]) - 96
        priority_sum += priority

print(priority_sum)
