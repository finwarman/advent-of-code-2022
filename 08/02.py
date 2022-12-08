#! /usr/bin/env python3

import numpy as np

# ==== INPUT ====

INPUT = 'input.txt'
with open(INPUT, 'r', encoding='UTF-8') as file:
    data = file.read()

rows = [[int(x) for x in list(row)] for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

W, H = len(rows[0]), len(rows)

grid = np.array(rows)

# edges 1, inner 0
vis = np.ones((W, H), dtype = int)
vis[1:-1,1:-1] = 0

result = 0

for row in range(H):
    for col in range(W):
        candidate = grid[row][col]
        sleft, sright, sup, sdown = 0,0,0,0
        for left in range(col-1, -1, -1):
            if grid[row][left] < candidate:
                sleft += 1
            else:
                sleft += 1
                break
        for right in range(col+1, W):
            if grid[row][right] < candidate:
                sright += 1
            else:
                sright += 1
                break
        for up in range(row-1, -1, -1):
            if grid[up][col] < candidate:
                sup += 1
            else:
                sup += 1
                break
        for down in range(row+1, H):
            if grid[down][col] < candidate:
                sdown += 1
            else:
                sdown += 1
                break
        scenic = sleft * sright * sup * sdown
        result = max(scenic, result)

print(result)

# output: 291840
assert result == 291840
