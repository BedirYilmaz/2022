import argparse
import numpy as np

parser = argparse.ArgumentParser(
    prog="Day2 Part 2",
    description="Find out your final score in an ideal scenario",
    epilog="AOC 2022 Day 2",
)

parser.add_argument("-f", "--filename")
args = parser.parse_args()

answer_scores = {"X": 1, "Y": 2, "Z": 3}
winner_hands = {"X": "Y", "Y": "Z", "Z": "X"}

most_frequent_answers = {}

rounds = np.loadtxt(args.filename, dtype=str)

total_score = 0

wins = rounds[rounds[:,1] == "X"]           
ties = rounds[rounds[:,1] == "Y"] 
loses = rounds[rounds[:,1] == "Z"] 

match_score = wins.shape[0] * 6 + ties.shape[0] * 3
# answer_score = 

print(total_score)
