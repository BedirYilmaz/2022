import argparse
import numpy as np


parser = argparse.ArgumentParser(
    prog="Day 5",
    description="",
    epilog="AOC 2022 Day 5",
)

parser.add_argument("-f", "--filename")
args = parser.parse_args()


stacks = []
with open(args.filename) as f:
    for line in f:
        if line == "\n":
            break
        stacks.append(np.array(list(line), dtype=str))
stacks_np = np.vstack(stacks)


stacks = []
for i, item in enumerate(stacks_np[-1,:]):
    if item.isalnum():
        stacks.append(list(reversed([e for e in stacks_np[:-1, i].tolist() if e is not " "])))
    

import re 
pattern = re.compile('[\W_]+')

flag = False
commands = []
with open(args.filename) as f:
    for line in f:
        if flag:
            commands.append(np.fromstring(line.replace("move", "").replace("from", "").replace("to", "").strip(), sep="  ", dtype=int))
        else:
            if line == "\n":
                flag = True
            else: 
                continue

print(stacks)

for command in commands:
    print(command)
    for _ in range(command[0]):
        item = stacks[command[1]-1].pop()
        stacks[command[2]-1].append(item)
    
for stack in stacks:
    print(stack[-1], end="")