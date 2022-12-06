import argparse
import numpy as np

parser = argparse.ArgumentParser(
    prog="Day2 Part 2",
    description="Find out your final score in an ideal scenario",
    epilog="AOC 2022 Day 2",
)

parser.add_argument("-f", "--filename")
args = parser.parse_args()

answer_scores = {"A": 1, "B": 2, "C": 3}
winner_hands = {"A": "B", "B": "C", "C": "A"}
loser_hands = {"A": "C", "B": "A", "C": "B"}


most_frequent_answers = {}

rounds = np.loadtxt(args.filename, dtype=str)

total_score = 0

wins = rounds[rounds[:,1] == "Z"]           
draws = rounds[rounds[:,1] == "Y"] 
loses = rounds[rounds[:,1] == "X"] 

match_score = wins.shape[0] * 6 + draws.shape[0] * 3
# answer_score = 

# get the winner hands for won rounds
won_hands = sum([answer_scores[winner_hands[item]] for item in wins[:, 0].tolist()])
# get the opponent moves for tie rounds
tie_hands = sum([answer_scores[item] for item in draws[:, 0].tolist()])
# get the losing hands for lost rounds
loser_hands = sum([answer_scores[loser_hands[item]] for item in loses[:, 0].tolist()])

total_score = match_score + won_hands + tie_hands + loser_hands

print(total_score)
