#! /usr/bin/env python3

import re

# ==== INPUT ====

INPUT = 'input.txt'
with open(INPUT, 'r', encoding='UTF-8') as file:
    data = file.read()

monkey_data = [[row.strip() for row in m.split('\n')] for m in data.split('\n\n')]

# ==== SOLUTION ====

class Monkey:
    def __init__(self, items, inspect, test):
        self.items    = items   # array[int]
        self.inspect  = inspect # lambda: new = func(old, x)
        self.test     = test    # lamdba: worry divisible by x
                                #        if true,  throw to y
                                #        if false, throw to z


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
    tests = f"lambda worry : ({true_to} if (worry % {divisor} == 0) else {false_to})"
    test = eval(tests)

    monkeys[index] = Monkey(items, inspect, test)

activity = [0 for _ in range(len(monkeys))]

for _ in range(20):
    for i, monkey in enumerate(monkeys):
        while monkey.items:
            worry = monkey.items.pop(0)
            worry = monkey.inspect(worry)
            worry = worry // 3
            target = monkey.test(worry)
            monkeys[target].items.append(worry)
            activity[i] += 1

for i, monkey in enumerate(monkeys):
    print(f"Monkey {i} inspected items {activity[i]} times")
print()

activity.sort()
result = activity[-2] * activity[-1]

print(result)

# output: 61503
# assert result == 61503
