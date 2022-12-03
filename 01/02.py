#! /usr/bin/env python3

# ==== INPUT ====

INPUT = 'input.txt'
with open(INPUT, 'r', encoding='UTF-8') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

totals = []
current = 0

for row in rows:
    if row:
        current += int(row)
    else:
        totals.append(current)
        current = 0

result = sum(sorted(totals, reverse=True)[:3])
print(result)

# output: 204639
assert result == 204639
