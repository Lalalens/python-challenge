# I'm inmporting my operating system to create a file path
import os

# Module for importing CSV files
import csv

# Module for reading CSV files
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Reading the csv files
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)
