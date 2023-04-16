# I'm inmporting my operating system to create a file path
import os

# Module for importing CSV files
import csv

print("Financial Analysis")
print("---------------------------")

# Module for reading CSV files
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# Reading the csv files
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
   # print(f"CSV Header: {csv_header}")

    #Set values
    total=0
    number_of_months = 0
    profit_losses = []
    changes = []
    previous_value = None

    #Calculate average and greatest and lowest total increases
    for row in csvreader:
        number_of_months += 1
        total += float(row[1])  
        profit_losses.append(float(row[1])) 
       


    # Find the average Profit/Losses
        if previous_value is not None:
           change = float(row[1]) - previous_value
           changes.append(change)

        

        previous_value = float(row[1])   


    average_change = round(sum(changes) / len(changes), 2)






    print(f"Total Month: {number_of_months}")
    print(f"Total: $ {total}")
    print(f"Average Change: {average_change}")
    