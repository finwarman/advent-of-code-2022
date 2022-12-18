#! /usr/bin/env python3

import re

# ==== INPUT ====

INPUT = 'input.txt'
with open(INPUT, 'r', encoding='UTF-8') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

beacons = set()
sensors = {}

# extract beacons, sensors, and grid dimensions
for row in rows:
    (sensor_x, sensor_y,
     beacon_x, beacon_y) = [
        int(x.group(1)) for x in re.finditer(r'=(-?\d+)\b', row)
    ]
    s = (sensor_x, sensor_y)
    b = (beacon_x, beacon_y)

    beacons.add(b)
    sensors[s] = b


MIN, MAX = 0, 4000000
# MIN, MAX = 0, 20

def manhattan(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])

ranges = {}
count = 0
for sensor, beacon in sensors.items():
    dist = manhattan(sensor, beacon)
    x, y = sensor

    count += 1
    print(f'{count}/{len(sensors)} items...')

    for row in range(max(MIN, y-dist), min(y+dist, MAX)+1):
        n = dist+1 - abs(row - y)
        width = (2*n-1) # nth odd number

        start = x - (width//2)
        rng = (max(MIN, start), min(start+width, MAX+1)-1)

        if row not in ranges:
            ranges[row] = set()
        ranges[row].add(rng)

# simplify ranges (merge intervals)
point = None
for y in range(MIN, MAX+1):
    intervals = [list(r) for r in sorted(ranges[y])]

    stack = []
    stack.append(intervals[0])
    for i in intervals[1:]:
        # merge overlapping intervals
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)

    if len(stack) == 1:
        continue

    if stack[0][1]+1 < stack[1][1]:
        point = (stack[0][1]+1, y)
        break

x, y = point
result = (4000000*x) + y

print(f"point: {x,y}")
print()
print(result)

# demo:
# assert result == 56000011

# output: 13213086906101
assert result == 13213086906101
