# Import operating system for file path
import os

#import csv file
import csv

print("Election Results")
print("------------------------")

#Module for readinf CSV files
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

#reading CSV files
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter="," )
    csv_header = next(csvreader)
 #  print(f"CSV Header: {csv_header}")

    #Set variables
    total_votes = 0
    candidates = {}
    

    #fiding the total votes and getting each candidates neame
    for row in csvreader:
        # same as below just short hand total_votes = total_votes + 1
        total_votes += 1
        candidate_name =row[2]
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        else:
            candidates[candidate_name] += 1


    print(f"Total Votes: {total_votes}")
    print("------------------------")
   

#Percentage of votes and candidates who won
max_votes = 0
winner = ""
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage: .3f}% ({votes})")
    
    #Find who won
    if votes > max_votes:
        max_votes = votes
        winner = candidate

print(f"Winner: {winner}")
print("-------------------------")



