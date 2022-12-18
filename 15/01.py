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


ROW = 2000000
# ROW = 10

def manhattan(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])

points = set()
for sensor, beacon in sensors.items():
    dist = manhattan(sensor, beacon)
    x, y = sensor

    if (ROW - y) > dist:
        continue

    n = dist+1 - abs(ROW - y)
    width = (2*n-1) # nth odd number

    start = x - (width//2)
    for i in range(start, start+width):
        p = (i, ROW)
        if p not in beacons:
            points.add(p)


total = len(points)

print(total)

# output: 5240818
assert total == 5240818
