import argparse
import numpy as np
import string

parser = argparse.ArgumentParser(
    prog="Day3 Part 2",
    description="Sum of the item priorities in rucksacks",
    epilog="AOC 2022 Day 3",
)

parser.add_argument("-f", "--filename")
args = parser.parse_args()

rucksacks = np.loadtxt(args.filename, dtype=str)

rucksacks_with_compartments = np.vstack([rucksacks, np.array([""]*rucksacks.shape[0]), np.array([""]*rucksacks.shape[0]) ])

common_item_types = []
for i in range(0, rucksacks.shape[0], 3):
    common_item_types.append(list(set(rucksacks[i]).intersection(set(rucksacks[i+1])).intersection(set(rucksacks[i+2])))[0])


alphabet_lowercase = list(string.ascii_lowercase)
alphabet_uppercase = list(string.ascii_uppercase)
alphabet = alphabet_lowercase + alphabet_uppercase

total_priorities = 0
for i in common_item_types:
    total_priorities += (alphabet.index(i)+1)
print(total_priorities)
