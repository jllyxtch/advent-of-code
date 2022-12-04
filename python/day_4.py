with open('input/input_4.txt', 'r') as f:
    full_overlaps = 0
    partial_overlaps = 0

    for line in f:
        assignment = [x.strip().split('-') for x in line.split(',')]
        assignment_expanded = [set(range(int(a), int(b)+1)) for [a, b] in assignment]

        # Part 1
        if assignment_expanded[0].issubset(
                assignment_expanded[1]) or assignment_expanded[1].issubset(
                assignment_expanded[0]):
            full_overlaps += 1

        # Part 2
        if assignment_expanded[0].intersection(assignment_expanded[1]):
            partial_overlaps += 1

print(full_overlaps)
print(partial_overlaps)
