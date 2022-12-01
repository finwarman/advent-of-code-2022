#! /usr/bin/env python3

# ==== INPUT ====
data = ""
with open('input.txt', 'r') as file:
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

print(sum(sorted(totals, reverse=True)[:3]))
