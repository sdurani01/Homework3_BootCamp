# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('election_data.csv')

# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)
    # creating variables that will be lists to count votes
    total_votes = []
    khan_votes = []
    correy_votes = []
    li_votes = []
    otooley_votes = []
    
    # for loop to count total votes, and votes for each candidate
    for row in csvreader:
        total_votes.append(row[2])
        if row[2] == "Khan":
            khan_votes.append(row[2])
        if row[2] == "Correy":
            correy_votes.append(row[2])
        if row[2] == "Li":
            li_votes.append(row[2])
        if row[2] == "O'Tooley":
            otooley_votes.append(row[2])

    # print out the results, with some calculations for percentages        
    print("Election Results")
    print("-----------------------------------")
    print("Total Votes: ", len(total_votes))
    print("-----------------------------------")
    print("Khan: ", str(round(len(khan_votes)/len(total_votes),2)*100) + "00%","(" + str(len(khan_votes)) + ")")
    print("Correy: ", str(round(len(correy_votes)/len(total_votes),2)*100) + "00%","(" + str(len(correy_votes)) + ")")
    print("Li: ", str(round(len(li_votes)/len(total_votes)*100,2)) + "00%","(" + str(len(li_votes)) + ")")
    print("O'Tooley: ", str(round(len(otooley_votes)/len(total_votes),2)*100) + "00%","(" + str(len(otooley_votes)) + ")")
    print("----------------------------------")
    
    # conditional flow to determine the winner
    if len(khan_votes) > len(correy_votes) and len(khan_votes) > len(li_votes) and len(khan_votes) > len(otooley_votes):
        print("Winner: Khan")
    elif len(correy_votes) > len(khan_votes) and len(correy_votes) > len(li_votes) and len(correy_votes) > len(otooley_votes):
        print("Winner: Correy")
    elif len(li_votes) > len(khan_votes) and len(li_votes) > len(correy_votes) and len(li_votes) > len(otooley_votes):
        print("Winner: Li")
    else: 
        print("Winner: O'Tooley")

