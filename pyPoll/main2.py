# open modules

import os
import csv

# set the total number of votes before the election begins equal to zero
total_votes = 0

# list the names of the candidates up for election

candidate_list = []
candidate_name = []

# set the vote counter and vote percentage for 4 candidates to zero


candidate_vote = [0, 0, 0, 0]
candidate_vote_percent = [0, 0, 0, 0]
candidate_winner = []

# define the path to the file that contains the results of the election
csvpath = os.path.join('Resources', 'election_data.csv')

# open the file as a csv file

with open(csvpath) as csvpath:

    csv_reader = csv.reader(csvpath, delimiter=',')
