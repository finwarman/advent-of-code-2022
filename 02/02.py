#! /usr/bin/env python3

# ==== INPUT ====
data = ''
f = 'input.txt'
with open(f, 'r', encoding='UTF-8') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

total = 0

# 1 win
# 2 paper
# 3 scissors

# 0 loss
# 3 draw
# 6 won

# X lose
# Y draw
# Z win

shapes = {
    'A': 1,
    'B': 2,
    'C': 3
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

loses = {
    'A': 'B',
    'B': 'C',
    'C': 'A'
}

score = 0
for row in rows:
    move, counter = row.split()
    counter_move = translate[counter]

    if counter == 'X':
        score += 0
        score += shapes[beats[move]]
        continue

    if counter == 'Z':
        score += 6
        score += shapes[loses[move]]
        continue

    # draw
    score += shapes[move]
    score += 3

print(score)
