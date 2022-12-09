import argparse
import numpy as np


parser = argparse.ArgumentParser(
    prog="Day 6",
    description="",
    epilog="AOC 2022 Day 6 2",
)

parser.add_argument("-f", "--filename")
args = parser.parse_args()


with open(args.filename) as f:
    code = next(iter(f))

print(code)

for i in range(4, len(code)):
    if len(set(code[i-4:i])) == 4:
        start = i+1
        break

for i in range(start+14, len(code)):
    if len(set(code[i-14:i])) == 14:
        print(i)
        break
