import os

import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

vote_list = []
otooley = []
khan = []
li = []
correy = []

candidates = ["O'tooley", "Khan", "Li", "Correy"]
total_candidate_votes = []



with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
 
    
    for row in csvreader:
        vote_list += [(row[2])]
        if row[2] =="Correy":
            #adds to Correy list
            correy.append(row[2])
        elif row[2] == "Li":
            li.append(row[2])
        elif row[2] == "Khan":
            khan.append(row[2])
        elif row[2] == "O'Tooley":
            otooley.append(row[2])
        else: 
            print("something is not right")



    candidate_names = list(set(vote_list))
    total_votes = len(vote_list)
    total_votes_correy = len(correy)
    total_votes_li = len(li)
    total_votes_khan = len(khan)
    total_votes_otooley = len(otooley)

    total_candidate_votes = (total_votes_otooley, total_votes_khan, total_votes_li, total_votes_correy)
    max_total_votes = max(total_votes_otooley, total_votes_khan, total_votes_li, total_votes_correy)
    max_votes_index = total_candidate_votes.index(max_total_votes)
    winner = candidates[max_votes_index]


    

    
    print(candidate_names)
    print(f'Total Votes: {total_votes}')
    print(f"O'Tooley: {total_votes_otooley/total_votes: .2%} ( {total_votes_otooley} )")
    print(f'Correy: {total_votes_correy/total_votes:.2%} ( {total_votes_correy} )' )
    print(f'Khan: {total_votes_khan/total_votes: .2%} ( {total_votes_khan} )')
    print(f'Li: {total_votes_li/total_votes: .2%} ( {total_votes_li} )') 
    print(f'Winner: {winner}')
    
    
    
    