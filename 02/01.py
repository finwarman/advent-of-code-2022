#! /usr/bin/env python3

# ==== INPUT ====
data = ''
f = 'input.txt'
with open(f, 'r', encoding='UTF-8') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

total = 0

# 1 rock
# 2 paper
# 3 scissors

# 0 loss
# 3 draw
# 6 won

shapes = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

translate = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

beats = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

score = 0
for row in rows:
    move, counter = row.split()
    score += shapes[counter]
    counter_move = translate[counter]

    if move == counter_move:
        score += 3
        continue
    if beats[counter_move] == move:
        score += 6
print(score)
