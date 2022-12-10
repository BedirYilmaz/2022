import argparse
import numpy as np

class Tree():

    def __init__(self, name, size=0):
        self.children = {}
        self.size = size

    def insert(self, name, size):
        self.children[name] = Tree(name, size)

    def chdir(self, name):
        return self.children[name]

    def sum(self):
        sum = 0
        for child in self.children:
            sum += child.sum()
        return sum

    def list_sums_of_dirs(self):
        sum = 0
        for child in self.children:
            sum += child.sum()
        return sum

parser = argparse.ArgumentParser(
    prog="Day 7",
    description="",
    epilog="AOC 2022 Day 7",
)

parser.add_argument("-f", "--filename")
args = parser.parse_args()

# read the logs

log = []
with open(args.filename) as f:
    for line in f:
        log.append(line)

log_np = np.vstack(log)

# parse the commands
root = Tree("/")
pwd = root
for i in range(log_np.shape[0]):
    line = log_np[i][0]
    if "$ ls" in line:
        print(line, end="")
    elif "$ cd .." in line:
        pwd = pwd.root
        print(line, end="")
    elif "$ cd /" in line:
        pwd = root
        print(line, end="")
    elif "$ cd" in line:
        pwd = pwd.chdir(line.replace("$ cd", "").strip())
        print(line, end="")
    elif "dir" in line.split(" ")[0]:
        print(line, end="")
    elif line.split(" ")[0].isnumeric():
        print(line, end="")
