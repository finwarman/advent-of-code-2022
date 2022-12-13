#! /usr/bin/env python3

import ast

# ==== INPUT ====

INPUT = 'input.txt'
with open(INPUT, 'r', encoding='UTF-8') as file:
    data = file.read()

pairs = [[row.strip() for row in m.strip().split('\n')] for m in data.split('\n\n')]

# ==== SOLUTION ====

pairs = [[ast.literal_eval(line) for line in pair] for pair in pairs]

def compare(lhs, rhs):
    if isinstance(lhs, list) and isinstance(rhs, int):
        return compare(lhs, [rhs])
    if isinstance(lhs, int) and isinstance(rhs, list):
        return compare([lhs], rhs)

    for i in range(min(len(lhs), len(rhs))):
        l, r = lhs[i], rhs[i]
        if isinstance(l, list) or isinstance(r, list):
            c = compare(l, r)
            if c is not None:
                return c
        elif l != r:
            return l < r

    if len(lhs) == len(rhs):
        return None
    return len(lhs) < len(rhs)

result = 0
for i, (lhs, rhs) in enumerate(pairs):
    if (compare(lhs, rhs)):
        result += i+1

print(result)

# output: 4821
assert result == 4821
