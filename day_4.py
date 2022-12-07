import argparse
import numpy as np
import string


parser = argparse.ArgumentParser(
    prog="Day 4",
    description="Find the number of fully contained assignment sections",
    epilog="AOC 2022 Day 4",
)

parser.add_argument("-f", "--filename")
args = parser.parse_args()

fully_contains_count = 0
with open(args.filename) as f:
    assignment_sections = np.loadtxt((line.replace(',','-') for line in f), delimiter="-", dtype=int)
    
for i in assignment_sections:
    if (i[0] <= i[2] and i[1] >= i[3]):
        fully_contains_count += 1
    elif (i[0] >= i[2] and i[1] <= i[3]):
        fully_contains_count += 1



print(fully_contains_count)