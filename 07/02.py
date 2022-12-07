#! /usr/bin/env python3
import re
import math

# ==== INPUT ====

INPUT = 'input.txt'
with open(INPUT, 'r', encoding='UTF-8') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

class Dir:
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.parent = None
        self.files = {}
        self.size = 0

    def PrintTree(self, required, indent='', results=[]):
        print(indent + self.name)
        print(indent + f'{self.size}')
        if self.size >= required:
            results.append(self.size)
        for dirname in sorted(self.children.keys()):
            child = self.children[dirname]
            results = child.PrintTree(required, indent + '  ', results)
        return results

    def CalculateSizes(self):
        self.size = sum(self.files.values())
        for dirname in sorted(self.children.keys()):
            child = self.children[dirname]
            child.CalculateSizes()
        if self.parent:
            self.parent.size += self.size

root = Dir('/')
current, prev = root, None

i = 0
while i < len(rows):
    row = rows[i]
    if row == '$ cd /':
        current = root
    elif row == '$ cd ..':
        current = current.parent
    elif row[0:4] == '$ cd':
        name = row.split(' ')[-1]
        prev = current
        current = current.children[name]
        current.parent = prev
    elif row == '$ ls':
        while i+1 < len(rows) and rows[i+1][0] != '$':
            i += 1
            row = rows[i]
            data, name = row.split(' ')
            if data == 'dir':
                if not name in current.children:
                    current.children[name] = Dir(name)
                dir = current.children[name]
            else:
                filesize = int(data)
                if not name in current.children:
                    current.files[name] = filesize
    i += 1


root.CalculateSizes()

unused = 70000000 - root.size

req = 30000000 - unused

totals = root.PrintTree(req)

result = min(totals)

print(result)

# output: 1112963
assert result == 1112963
