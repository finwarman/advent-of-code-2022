#! /usr/bin/env python3

# ==== INPUT ====

INPUT = 'input.txt'
with open(INPUT, 'r', encoding='UTF-8') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

class Dir:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = {}
        self.files = {}
        self.size = 0

    def get_answer(self, total=0):
        if self.size <= 100000:
            total += self.size
        for dirname in sorted(self.children.keys()):
            child = self.children[dirname]
            total = child.get_answer(total)
        return total

    def calculate_sizes(self):
        self.size = sum(self.files.values())
        for dirname in sorted(self.children.keys()):
            child = self.children[dirname]
            child.calculate_sizes()
        if self.parent:
            self.parent.size += self.size


root = Dir('/')

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
            else:
                filesize = int(data)
                if not name in current.children:
                    current.files[name] = filesize
    i += 1


root.calculate_sizes()
total = root.get_answer()

print(total)

# output: 1792222
assert total == 1792222
