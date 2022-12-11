import argparse
import numpy as np


parser = argparse.ArgumentParser(
    prog="Day 8",
    description="Find the number of visible trees",
    epilog="AOC 2022 Day 8",
)

parser.add_argument("-f", "--filename")
args = parser.parse_args()

# read the map

map = []
with open(args.filename) as f:
    for line in f:
        map.append(np.array(list(line.strip()), dtype=int))

map_np = np.vstack(map)

total_visible = 0

print(map_np.shape)
visibles = np.zeros(map_np.shape, dtype=int)

for i in range(map_np.shape[0]):
    for j in range(map_np.shape[1]):
        if np.all(map_np[i,j] > map_np[i+1:,j]) or np.all(map_np[i,j] > map_np[:i,j]) or np.all(map_np[i,j] > map_np[i,j+1:]) or np.all(map_np[i,j] > map_np[i,:j]):
            visibles[i,j] = True

print(map_np)
print(visibles)

print(visibles.sum())