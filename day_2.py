import argparse
import numpy as np

parser = argparse.ArgumentParser(
    prog="Day1 Part 2",
    description="Find out if the elf is fooling you or not",
    epilog="AOC 2022 Day 1",
)

parser.add_argument("-f", "--filename")
args = parser.parse_args()

answer_scores = {"A": 1, "B": 2, "C": 3}
winner_hands = {"A": "B", "B": "C", "C": "A"}
aliases = {"A": "X", "B": "Y", "C": "Z"}

most_frequent_answers = {}

rounds = np.loadtxt(args.filename, dtype=str)

for move in answer_scores.keys():
    answers = rounds[rounds[:, 0] == move][:, 1]
    values, counts = np.unique(answers, return_counts=True)

# score_for_answer = answer_scores[most_freq_answer]
# total_score = (score_for_answer + 3) * counts[ind]
