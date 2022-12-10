import argparse

parser = argparse.ArgumentParser(
    prog="Day1", description="Find the richest elf", epilog="AOC 2022 Day 1"
)

parser.add_argument("-f", "--filename")
args = parser.parse_args()

list_of_elves = []

with open(args.filename) as f:
    lines = f.readlines()
    elf = 0
    for line in lines:
        if line == "\n":
            list_of_elves.append(elf)
            elf = 0
            continue
        elf += (int(line))


print(max(list_of_elves))
