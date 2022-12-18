#! /usr/bin/env python3

# ==== INPUT ====

INPUT = 'input.txt'
with open(INPUT, 'r', encoding='UTF-8') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

c = []
for row in rows:
    x, y, z = [int(i) for i in row.split(',')]
    c.append((x,y,z))

cubes = set(c)

faces = 0
for cube in c:
    x, y, z = cube
    exposed = 6

    for dx, dy, dz in [
        (-1, 0, 0),( 1, 0, 0),
        ( 0,-1, 0),( 0, 1, 0),
        ( 0, 0,-1),( 0, 0, 1),
    ]:
        new = (x+dx, y+dy, z+dz)
        if new != cube and new in cubes:
            exposed -= 1
            
    faces += exposed

print(faces)

# output: 3390
assert faces == 3390
