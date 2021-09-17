import os

import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

vote_list = []
otooley = []
khan = []
li = []
correy = []


#candidate_names = list(set(candidates))

num_vote = []



with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    num_votes = 0
    
    
    
    
    
    for row in csvreader:
        num_votes += 1
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
    



    #Percentage_of_Votes = sum(candidate_votes) Number of cadidate votes / (num_votes) total number votes
    

          
    
    
    print(total_votes)
    print(f'Correy: {total_votes_correy} ' )
    print(f'Li: {total_votes_li}')
    print(f'Khan: {total_votes_khan}')
    print(f"O'Tooley: {total_votes_otooley}")
    print(str(num_votes))
    print(candidate_names)
    