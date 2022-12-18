#! /usr/bin/env python3

from operator import itemgetter

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

W = max(c,key=itemgetter(0))[0] + 2
H = max(c,key=itemgetter(1))[1] + 3
D = max(c,key=itemgetter(2))[2] + 2
print(W,H,D)

slices = [[[' ' for _ in range(W)] for _ in range(H)] for _ in range(D)]

for x,y,z in c:
    slices[z][y+1][x] = '#'


cubes = set(c)

air = {} # neighbours of air

for cube in c:
    x, y, z = cube
    for dx, dy, dz in [
        (-1, 0, 0),( 1, 0, 0),
        ( 0,-1, 0),( 0, 1, 0),
        ( 0, 0,-1),( 0, 0, 1),
    ]:
        new = (x+dx, y+dy, z+dz)
        if new not in cubes:
            if new not in air:
                air[new] = set()
            air[new].add(cube)


internal_air = set()

# flood fill to determine internal or external
checked = set()
for a in air:
    if a in checked:
        continue
    checked.add(a)
    group = set([a])
    external = False
    queue = [a]
    while queue:
        x,y,z = queue.pop()
        for dx, dy, dz in [
                (-1, 0, 0),( 1, 0, 0),
                ( 0,-1, 0),( 0, 1, 0),
                ( 0, 0,-1),( 0, 0, 1),
        ]:
            nx,ny,nz = new = (x+dx, y+dy, z+dz)
            if (nx < 0 or nx > W) or (ny < 0 or ny > H) or (nz < 0 or nz > D):
                external = True
                continue
            if (new not in cubes) and (new not in group) and (new not in checked):
                group.add(new)
                checked.add(new)
                queue.append(new)

    if not external:
        for a in group:
            internal_air.add(a)

for air in internal_air:
    x,y,z = air
    slices[z][y+1][x] = 'i'


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
        if new != cube and (
            new in cubes or
            new in internal_air
        ):
            exposed -= 1

    faces += exposed


# output cube
# for i in range(D):
#     print()
#     print(f'z={i}:')
#     print('_'*W)
#     grid = slices[i]
#     for row in grid:
#         print(''.join(row))
#     print('_'*W)

print()
print(faces)

# output: 2058
assert faces == 2058
