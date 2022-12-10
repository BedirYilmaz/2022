import argparse
import numpy as np
import string

parser = argparse.ArgumentParser(
    prog="Day3 Part 1",
    description="Sum of the item priorities in rucksacks",
    epilog="AOC 2022 Day 3",
)

parser.add_argument("-f", "--filename")
args = parser.parse_args()

rucksacks = np.loadtxt(args.filename, dtype=str)

rucksacks_with_compartments = np.vstack([rucksacks, np.array([""]*rucksacks.shape[0]), np.array([""]*rucksacks.shape[0]) ])

common_item_types = []
for i in range(rucksacks.shape[0]):
    rucksacks_with_compartments[1,i] = rucksacks_with_compartments[0,i][:int(len(rucksacks_with_compartments[0,i])/2)]
    rucksacks_with_compartments[2,i] = rucksacks_with_compartments[0,i][int(len(rucksacks_with_compartments[0,i])/2):]

    common_item_types.append(list(set(rucksacks_with_compartments[1,i]).intersection(set(rucksacks_with_compartments[2,i])))[0])  


alphabet_lowercase = list(string.ascii_lowercase)
alphabet_uppercase = list(string.ascii_uppercase)
alphabet = alphabet_lowercase + alphabet_uppercase

total_priorities = 0
for i in common_item_types:
    total_priorities += (alphabet.index(i)+1)
print(total_priorities)
