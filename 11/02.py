#! /usr/bin/env python3

from collections import deque
import re
import numpy as np

# import sys
# sys.set_int_max_str_digits(0)

# ==== INPUT ====

INPUT = 'input.txt'
with open(INPUT, 'r', encoding='UTF-8') as file:
    data = file.read()

monkey_data = [[row.strip() for row in m.split('\n')] for m in data.split('\n\n')]

# ==== SOLUTION ====

class Monkey:
    def __init__(self, items, inspect, divisor, truemonkey, falsemonkey):
        self.items   = deque(items) # array[int]
        self.inspect = inspect      # lambda: new = func(old, x)
        self.divisor = divisor
        self.truemonkey  = truemonkey
        self.falsemonkey = falsemonkey


monkeys = [None for _ in range(len(monkey_data))]

for rows in monkey_data:
    index = int(rows[0][-2])
    items = [int(x) for x in re.split(r'[^\d]+', rows[1])[1:]]

    # build operation function
    ops = f"lambda old : ({rows[2].split('= ')[1]})"
    inspect = eval(ops)

    # build test function
    divisor = int(rows[3].split(' ')[-1])
    true_to, false_to = int(rows[4][-1]), int(rows[5][-1])

    monkeys[index] = Monkey(items, inspect, divisor, true_to, false_to)

activity = [0 for _ in range(len(monkeys))]

# get a common factor of all the divisor checks
normalise = int(np.product([m.divisor for m in monkeys]))

for r in range(10000):
    for i, monkey in enumerate(monkeys):
        while monkey.items:
            worry = monkey.items.popleft()
            worry = monkey.inspect(worry)

            target = monkey.falsemonkey
            if worry % monkey.divisor == 0:
                target = monkey.truemonkey

            worry = worry % normalise

            monkeys[target].items.append(worry)

            activity[i] += 1

    # debug output
    if (r+1) % 1000 == 0:
        print(f"== After round {r+1} ===")
        for i, monkey in enumerate(monkeys):
            print(f"Monkey {i} inspected items {activity[i]} times")
        print()

activity.sort()
result = activity[-2] * activity[-1]

print(result)

# output: 14081365540
assert result == 14081365540
