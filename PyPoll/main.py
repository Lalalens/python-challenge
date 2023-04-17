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



    for row in csvreader:
        total_votes += 1


    print(f"Total Votes: {total_votes}")
    print("--------------------------")


