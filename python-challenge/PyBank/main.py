# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('budget_data.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip the header row
    next(csvreader)

    # Define variables, some as blank lists, others as numbers
    pnl = []
    date = []
    pnl_change = []
    avg_pnl_change = 0
    max_pnl_change = 0
    min_pnl_change = 0
    max_pnl_change_date = []
    min_pnl_change_date = []

    # create for loop to sum the column 1 which is pnl in the file and counted total months which is column 0 
    for row in csvreader:

        pnl.append(float(row[1]))
        date.append(row[0])

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total Profits and Losses: $", int(sum(pnl)))


    # Create for loop to get the total of difference between all row of column "Profits & Losses" and found total pnl change. 
    # Also calculated max pnl change and min pnl change. 
    for i in range(1,len(pnl)):
        pnl_change.append(pnl[i] - pnl[i-1])   
        avg_pnl_change = sum(pnl_change)/len(pnl_change)

        max_pnl_change = max(pnl_change)

        min_pnl_change = min(pnl_change)

        max_pnl_change_date = str(date[pnl_change.index(max(pnl_change))])
        min_pnl_change_date = str(date[pnl_change.index(min(pnl_change))])


    print("Average P/L Change: $", round(avg_pnl_change))
    print("Greatest Increase in P/L:", max_pnl_change_date,"($", int(max_pnl_change),")")
    print("Greatest Decrease in P/L:", min_pnl_change_date,"($", int(min_pnl_change),")")