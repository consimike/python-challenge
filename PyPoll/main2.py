import os

import csv

csvpath = "election_data.csv"

# Method 2: Improved Reading using CSV module

with open(csvpath, newline='', encoding= 'utf-8') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader) # reads the 0 row 
    
    print(f"{csv_header}")
    prevVote = 0
    total_votes = 0
    count = 0
    candidate = []
    Khan= 0
    OTool=0
    Correy = 0
    Li = 0
    for row in csvreader:
        voter_id = row[0]
        cand_name = row[2]

        if voter_id == prevVote:
            voter_id = prevVote
        else: 
            total_votes = total_votes + 1

        prevVote = voter_id

        if cand_name not in candidate:
            candidate.append(row[2])
        if cand_name == candidate[0]:
            Khan = Khan + 1
        if cand_name == "Correy":
            Correy = Correy + 1
        if cand_name == "Li":
            Li = Li + 1
        if cand_name == "O'Tooley":
            OTool = OTool + 1
        
    percentK = round((Khan / total_votes) *100,3)
    percentC = round((Correy / total_votes)*100,3)
    percentL = round((Li/total_votes)*100,3)
    percentO = round((OTool/total_votes)*100,3)

    winner = max(percentC,percentK,percentL,percentO)

    print("Election Results")
    print (f"Total votes: {total_votes}")
    print(f"Candidates {candidate}")
    print (f"{percentK}% {Khan}")
    print(f"{percentC}% {Correy}")
    print(f"{percentL}% {Li}")
    print (f"{percentO}% {OTool}")
    print(f"Winner: {winner}")
    