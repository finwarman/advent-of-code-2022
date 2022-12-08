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

# left-right
for row in range(1, H):
    gmax = grid[row][0]
    for col in range(1, W):
        gmax = max(grid[row][col-1], gmax)
        if grid[row][col] > gmax:
            vis[row][col] = 1

# right-left
for row in range(1, H):
    gmax = grid[row][-1]
    for col in range(W-2, 0, -1):
        gmax = max(grid[row][col+1], gmax)
        if grid[row][col] > gmax:
            vis[row][col] = 1

# top-bottom
for col in range(1, W):
    gmax = grid[0][col]
    for row in range(1, H-1):
        gmax = max(grid[row-1][col], gmax)
        if grid[row][col] > gmax:
            vis[row][col] = 1

# bottom-top
for col in range(1, W):
    gmax = grid[-1][col]
    for row in range(H-2, 0, -1):
        gmax = max(grid[row+1][col], gmax)
        if grid[row][col] > gmax:
            vis[row][col] = 1

# print(vis)

result = np.sum(vis)
print(result)

# output: 1829
assert result == 1829
