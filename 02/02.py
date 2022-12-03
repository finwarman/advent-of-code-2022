#! /usr/bin/env python3

# ==== INPUT ====
data = ''
f = 'input.txt'
with open(f, 'r', encoding='UTF-8') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

scores = {'A': 1, 'B': 2, 'C': 3}

beats = {'A': 'C', 'B': 'A', 'C': 'B'}
loses = {'A': 'B', 'B': 'C', 'C': 'A'}

score = 0
for row in rows:
    move, counter = row.split()
    # must lose
    if counter == 'X':
        score += 0
        score += scores[beats[move]]
        continue
    # must win
    if counter == 'Z':
        score += 6
        score += scores[loses[move]]
        continue
    # draw
    score += scores[move]
    score += 3

print(score)

# output: 13187
assert score == 13187
