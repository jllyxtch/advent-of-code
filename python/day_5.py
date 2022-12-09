lines = [line.rstrip('\n') for line in open('input/input_5.txt')]
stack = lines[:lines.index('')]
instructions = lines[lines.index('')+1:]
new_stack = []

for i, row in enumerate(stack):
    new_row = []
    for j in range(9):
        new_row.append(row[j*4+1])
    new_stack.append(new_row)

rotated_stack = [[] for _ in range(10)]
for i in range(1, len(new_stack)):
    for j, box in enumerate(new_stack[-i-1]):
        if not box == ' ':
            rotated_stack[j+1].append(box)

new_instructions = []
for instruction in instructions:
    new_instruction = instruction.split(' ')
    new_instructions.append(
        [int(new_instruction[1]),
         int(new_instruction[3]),
         int(new_instruction[5])])

rotated_stack_1 = rotated_stack
for instruction in new_instructions:
    for i in range(instruction[0]):
        rotated_stack_1[instruction[2]].append(rotated_stack_1[instruction[1]].pop(-1))

rotated_stack_2 = rotated_stack
for instruction in new_instructions:
    move = instruction[0]
    rotated_stack_2[instruction[2]].extend(rotated_stack_2[instruction[1]][-move:])
    del rotated_stack_2[instruction[1]][instruction[0]*-1:]

top = ''
for row in rotated_stack_2:
    if row:
        top = top + row[-1]

print(top)
