# Import operating system for file path
import os

#import csv file
import csv

#Module for readinf CSV files
csvpath = os.path.join('.', 'Resources', 'election_data.csv') # './Resources/election_data.csv'

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
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        else:
            candidates[candidate_name] += 1

#Percentage of votes and candidates who won
max_votes = 0
winner = ""

print("Election Results")
print("------------------------")

print(f"Total Votes: {total_votes}")
print("------------------------")

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {round(percentage, 3)}% ({votes})")
    
    #Find who won
    if votes > max_votes:
        max_votes = votes
        winner = candidate
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

with open('./analysis/results.txt', 'w') as file:
    file.write(("Election Results"))
    file.write(("------------------------"))
    file.write((f"Total Votes: {total_votes}"))
    file.write(("------------------------"))
    file.write((f"{candidate}: {round(percentage, 3)}% ({votes})"))
    file.write(("-------------------------"))
    file.write((f"Winner: {winner}"))
    file.write(("-------------------------"))
    



