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

scenic_scores = np.zeros(map_np.shape, dtype=int)

def sum_visibles(reference, arr):

    visibles = np.zeros(arr.shape).astype(bool)
    for i in range(len(arr)):
        if arr[i] < reference: 
            if np.all(arr[i]>=arr[:i]):
                visibles[i] = True
        else:
            visibles[i] = True
            # print(reference, arr, visibles)
            return np.sum(visibles)
    # print(reference, arr, visibles)
    return np.sum(visibles)



for i in range(map_np.shape[0]):
    for j in range(map_np.shape[1]):
        
        # if i == 3 and j == 2:
        # print(np.flip(map_np[:i,j]))
        # print(map_np[i+1:,j])
        # print(np.flip(map_np[i,:j]))
        # print(map_np[i,j+1:])
        up_score = sum_visibles(map_np[i,j], np.flip(map_np[:i,j]))
        down_score = sum_visibles(map_np[i,j], map_np[i+1:,j])
        left_score = sum_visibles(map_np[i,j], np.flip(map_np[i,:j]))
        right_score = sum_visibles(map_np[i,j], map_np[i,j+1:])
        scenic_scores[i,j] = up_score * down_score * left_score * right_score

        
# after a smaller tree that is not larger than its adjacent, one needs to trace through until coming to a tree greater than reference
# a tree can occlude another only if it has the same or greater height
# r (i.e. 9) -> 4 -> 5 -> 6 -> 6 -> 7 -> 8 -> 8 -> 9  

print(map_np)
print(scenic_scores)
print(scenic_scores.max())