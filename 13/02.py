#! /usr/bin/env python3

import ast
import functools

# ==== INPUT ====

INPUT = 'input.txt'
with open(INPUT, 'r', encoding='UTF-8') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1] if row]

# ==== SOLUTION ====

rows = [ast.literal_eval(row) for row in rows]
rows.append([[2]])
rows.append([[6]])

def compare(lhs, rhs):
    if isinstance(lhs, list) and isinstance(rhs, int):
        rhs = [rhs]
        return compare(lhs, rhs)
    elif isinstance(lhs, int) and isinstance(rhs, list):
        lhs = [lhs]
        return compare(lhs, rhs)
    for i in range(max(len(lhs), len(rhs))):
        if i >= len(lhs):
            return True
        elif i >= len(rhs):
            return False
        l, r = lhs[i], rhs[i]
        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                return True
            if l > r:
                return False
        else:
            c = compare(l, r)
            if c is not None:
                return c
    return None

def cmp(lhs, rhs):
    c = compare(lhs, rhs)
    if c is True:
        return 1
    elif c is False:
        return -1
    return 0

rows = sorted(rows, key=functools.cmp_to_key(cmp), reverse=True)
result = (rows.index([[2]]) + 1) * (rows.index([[6]]) + 1)

print(result)

# output: 21890
assert result == 21890
