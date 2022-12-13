#! /usr/bin/env python3

import ast
import functools

# ==== INPUT ====

INPUT = 'input.txt'
with open(INPUT, 'r', encoding='UTF-8') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1] if row]

# ==== SOLUTION ====

SEP1, SEP2 = [[2]], [[6]]
rows = [ast.literal_eval(row) for row in rows] + [SEP1, SEP2]

def compare(lhs, rhs):
    if isinstance(lhs, list) and isinstance(rhs, int):
        return compare(lhs, [rhs])
    if isinstance(lhs, int) and isinstance(rhs, list):
        return compare([lhs], rhs)

    for i in range(min(len(lhs), len(rhs))):
        l, r = lhs[i], rhs[i]
        if isinstance(l, list) or isinstance(r, list):
            return compare(l, r)
        elif l != r:
            return l < r

    return len(lhs) < len(rhs)

def cmp(lhs, rhs):
    return (1 if compare(lhs, rhs) else -1)

rows = sorted(rows, key=functools.cmp_to_key(cmp), reverse=True)
result = (rows.index(SEP1)+1) * (rows.index(SEP2)+1)

print(result)

# output: 21890
assert result == 21890
