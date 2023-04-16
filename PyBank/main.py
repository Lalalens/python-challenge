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
    greatest_increase = -float('inf')
    greatest_decrease = float('inf')
    greatest_increase_date = ""
    greatest_decrease_date = ""

    # Total number of months and total Profit/Losses 
    for row in csvreader:
        number_of_months += 1
        total += float(row[1])  
        profit_losses.append(float(row[1])) 
       
 

    # Find the chnages in Proft/Losses and average changes
        if previous_value is not None:
           change = float(row[1]) - previous_value
           changes.append(change)

           # Fing the greatest increase and decrease over the entire period
           if change > greatest_increase:
               greatest_increase = round(change)
               greatest_increase_date = row[0]
           elif change < greatest_decrease:
               greatest_decrease = round(change)
               greatest_decrease_date = row[0]


        

        previous_value = float(row[1])   


    average_change = round(sum(changes) / len(changes), 2)






    print(f"Total Month: {number_of_months}")
    print(f"Total: $ {total}")
    print(f"Average Change: {average_change}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f" Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
    