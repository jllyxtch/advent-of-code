with open('input/input_6.txt', 'r') as f:
    buffer = f.read()

n = 14  # Length of marker
for i, character in enumerate(buffer):
    if i >= n:
        unique_letters = set(buffer[i-n:i])
        if len(unique_letters) == n:
            print(i)
