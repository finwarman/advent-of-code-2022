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


# MIN, MAX = 0, 4000000
MIN, MAX = 0, 20

def manhattan(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])

points = set()
count = 0
for sensor, beacon in sensors.items():
    dist = manhattan(sensor, beacon)
    x, y = sensor

    count += 1
    print(f'{count}/{len(sensors)} items...')

    for row in range(max(MIN, y-dist), min(y+dist, MAX)+1):
        n = dist+1 - abs(row - y)
        width = (2*n-1) # nth odd number

        # TODO: convert to ranges

        start = x - (width//2)
        for i in range(max(MIN, start), min(start+width, MAX+1)):
            p = (i, row)
            points.add(p)

print()
result = 0
for x in range(MIN, MAX+1):
    for y in range(MIN, MAX+1):
        if (x,y) not in points:
            print(f"point: {x,y}")
            result = (4000000*x)+y
            break
    else:
        continue
    break

print()
print(result)

# output: 0
# assert result == 0

# demo:
assert result == 56000011
