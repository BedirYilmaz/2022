import argparse
import numpy as np

class Tree():

    def __init__(self, name, size=0):
        self.root = None
        self.children = {}
        self.size = size
        self.name = name

    def insert(self, name, size=0):
        self.children[name] = Tree(name, size)
        self.children[name].root = self

    def chdir(self, name):
        return self.children[name]

    def sum(self):
        sum = 0
        for child in self.children:
            sum += child.sum()
        return sum

    def list_sums_of_dirs(self):
        c_sum = 0
        c_folders = []
        for child_name in self.children.keys():
            child = self.children[child_name]
            if len(child.children.keys()) is not 0:
                l_sum, l_folders = child.list_sums_of_dirs()
                c_sum = c_sum + l_sum
                if l_sum < 100000:
                    l_folders.append(l_sum)
                c_folders.extend(l_folders)
            c_sum += child.size
        return c_sum, c_folders


    def traverseInorder(self):
        """
        traverse function will print all the node in the tree.
        """
        if len(self.children) == 0:
            print(self.name, self.size, end=", ")

        for child_name in self.children.keys():
            self.children[child_name].traverseInorder()
        if self.size == 0:
            print("eod")



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

verbose = False
root = Tree("/")
for i in range(log_np.shape[0]):
    line = log_np[i][0]
    if "$ cd /" in line:
        pwd = root
        if verbose:
            print("root directory")
    elif "$ cd .." in line:
        pwd = pwd.root
        if verbose:
            print("upper directory")
    elif "$ cd" in line:
        if verbose:
            print(f"changing directory {line.split(' ')[-1].strip()}")
        pwd = pwd.chdir(line.split(" ")[-1].strip())
    elif "dir" in line.split(" ")[0]:
        dirname = line.split(' ')[-1].strip() 
        if verbose:
            print(f"inserting directory {dirname}")
        pwd.insert(line.split(" ")[-1].strip(), 0)
    elif line.split(" ")[0].isnumeric():
        if verbose:
            print(f"inserting file {line.split(' ')[-1].strip()} {line.split(' ')[0].strip()}")
        pwd.insert(line.split(" ")[-1].strip(), int(line.split(" ")[0]))
        
csum, c_folders = root.list_sums_of_dirs()

print(sum(c_folders))