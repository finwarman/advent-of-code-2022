#! /usr/bin/env python3

import ast

# ==== INPUT ====

INPUT = 'input.txt'
with open(INPUT, 'r', encoding='UTF-8') as file:
    data = file.read()

pairs = [[row.strip() for row in m.strip().split('\n')] for m in data.split('\n\n')]

# ==== SOLUTION ====

pairs = [[ast.literal_eval(line) for line in pair] for pair in pairs]

def compare(lhs, rhs, indent=''):
    print(f"{indent}- Compare {lhs} vs {rhs}")
    indent = '  ' + indent

    if isinstance(lhs, list) and isinstance(rhs, int):
        rhs = [rhs]
        print(f"{indent}- Mixed types; convert right to {rhs} and retry comparison")
        return compare(lhs, rhs, indent)
    elif isinstance(lhs, int) and isinstance(rhs, list):
        lhs = [lhs]
        print(f"{indent}- Mixed types; convert left to {lhs} and retry comparison")
        return compare(lhs, rhs, indent)

    for i in range(max(len(lhs), len(rhs))):
        if i >= len(lhs):
            print(f"{indent}- Left side ran out of items, so inputs are in the right order")
            return True
        elif i >= len(rhs):
            print(f"{indent}- Right side ran out of items, so inputs are not in the right order")
            return False
        l, r = lhs[i], rhs[i]

        if isinstance(l, int) and isinstance(r, int):
            print(f"{indent}- Compare {l} vs {r}")
            if l < r:
                print(f"  {indent}- Left side is smaller, so inputs are in the right order")
                return True
            if l > r:
                print(f"  {indent}- Right side is smaller, so inputs are not in the right order")
                return False
        else:
            result = compare(l, r, indent)
            if result is not None:
                return result

    return None


result = 0
for i, (lhs, rhs) in enumerate(pairs):
    print(f"== Pair {i+1} ==")
    if (compare(lhs, rhs)):
        result += i+1
    print()

print(result)

# output: 4821
assert result == 4821
