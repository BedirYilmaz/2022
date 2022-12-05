import argparse
import numpy as np

parser = argparse.ArgumentParser(
    prog="Day1 Part 2",
    description="Find out if the elf is fooling you or not",
    epilog="AOC 2022 Day 1",
)

parser.add_argument("-f", "--filename")
args = parser.parse_args()

answer_scores = {"X": 1, "Y": 2, "Z": 3}
winner_hands = {"X": "Y", "Y": "Z", "Z": "X"}
aliases = {"A": "X", "B": "Y", "C": "Z"}

most_frequent_answers = {}

rounds = np.loadtxt(args.filename, dtype=str)

total_score = 0
for opponents_move in aliases.keys():
    answers = rounds[rounds[:, 0] == opponents_move][:, 1]
    values, counts = np.unique(answers, return_counts=True)

    number_of_ties = counts[values == aliases[opponents_move]]
    number_of_wins = counts[values == winner_hands[aliases[opponents_move]]]
    number_of_fails = counts.sum() - (number_of_ties + number_of_wins)

    total_score_from_answers = np.array([a*b for a,b in zip([answer_scores[vi] for vi in values], counts)]).sum()

    total_score += number_of_ties * 3 + number_of_wins * 6 + total_score_from_answers 

print(total_score)
