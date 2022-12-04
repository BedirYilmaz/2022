import argparse

parser = argparse.ArgumentParser(
    prog="Day1 Part 2", description="Find how many total fruits the top three richest elves have", epilog="AOC 2022 Day 1"
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


total_number_of_fruits = 0

for i in range(3):
    index, item = max(enumerate(list_of_elves), key=lambda x: x[1])
    total_number_of_fruits += item
    list_of_elves.pop(index)


print(total_number_of_fruits)
