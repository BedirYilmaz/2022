import argparse
import numpy as np


parser = argparse.ArgumentParser(
    prog="Day 6",
    description="",
    epilog="AOC 2022 Day 6",
)

parser.add_argument("-f", "--filename")
args = parser.parse_args()


with open(args.filename) as f:
    code = next(iter(f))

print(code)

for i in range(4, len(code)):
    if len(set(code[i-4:i])) == 4:
        print(i+1)
        break
