#! /usr/bin/env python3

from collections import deque

# ==== INPUT ====

INPUT = 'input.txt'
with open(INPUT, 'r', encoding='UTF-8') as file:
    data = file.read()

grid = [list(row.strip()) for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

W, H = len(grid[0]), len(grid)

# find start / end positions
start = (0,0)
end = (0,0)
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char == 'S':
            start = (x,y)
            grid[y][x] = 'a'
        elif char == 'E':
            end = (x,y)
            grid[y][x] = 'z'

# convert to numeric
grid = [[ord(char)-96 for char in row] for row in grid]

def candidates(pos, grid, visited):
    x,y = pos
    cands = []
    val = grid[y][x]
    for dy, dx in [(-1, 0),(0,-1),(0,1),(1,0)]:
        nx, ny = x+dx, y+dy
        if nx < W and nx >= 0 and ny < H and ny >= 0:
            cand = (nx, ny)
            nval = grid[ny][nx]
            if (cand not in visited) and ((nval-val) <= 1):
                cands.append(cand)
    return cands

def path(parents, end):
    path = []
    u = end
    while u is not None:
        path.append(u)
        u = parents[u]
    return path

result = None
parents = {
    start: None
}

c = deque([start])
visited = set([start])
while c and not result:
    u = c.popleft()
    visited.add(u)
    for v in candidates(u, grid, visited.union(c)):
        parents[v] = u
        if v == end:
            result = len(path(parents, v)) - 1
            break
        c.append(v)

print(result)

# output: 534
assert result == 534
