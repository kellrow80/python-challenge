import os

import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

candidates = []

#candidate_names = list(set(candidates))

num_vote = []



with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    num_votes = 0
    total = 0
    
    
    
    
    for row in csvreader:
        num_votes += 1
        total += int(row[0])
        candidates += [(row[2])]

    #candidate_names = list(set(candidates))          
    
    

    print(str(num_votes))
    #print(candidates_names)