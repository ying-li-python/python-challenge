""" 
This script is designed to analyze poll data 

Results will return: 
Total Votes
Percentage/Votes per candidate
Winner of the election

"""


# import dependencies
import os
import csv


# find path for csv file 
pollCSV = os.path.join(os.path.dirname(__file__), 'Resources', 'election_data.csv')


# create variable to datafile
with open(pollCSV, 'r') as polldata: 

    # initiate reader
    reader = csv.reader(polldata)

    # skip header
    next(reader)

    # generate list comphrehension of votes per candidate
    candidate_votes = [row[2] for row in reader]

    # solution to calculate the total number of votes 
    voter_count = len(candidate_votes)

    # create empty dictionary to hold candidate counts
    d = {}

    # create for loop that matches unique candidate and generate vote count 
    for names in set(candidate_votes): 
        key = names 
        votes = candidate_votes.count(names)
        percentage = round((votes / voter_count) * 100, 2) 
        percentage = "{}%".format(percentage)
        votes = "({})".format(votes)
        d[key] = percentage, votes 


    # generate results in output file and print in terminal 
    with open("output.txt", "w") as output_file:

        output_file.write("Election Results" + "\n")
        output_file.write("------------------" + "\n")
        output_file.write(f"Total votes: {voter_count}" + "\n")
        output_file.write("------------------" + "\n")

        print("Election Results")
        print("------------------")
        print(f"Total votes: {voter_count}")
        print("------------------")

        for key, votes in d.items():
            percentage= str(votes[0])
            votes = str(votes[1])
            print(str(key) + ": " + str(percentage) + " " + str(votes))  
            winner = max(d, key=lambda key:d[key])    
            results = str(key) + ": " + str(percentage) + " " + str(votes) + "\n"
            output_file.write(results)

        print("------------------")
        print("Winner: " + str(winner))
        print("------------------")


        output_file.write("------------------" + "\n")
        output_file.write(f"Winner : {winner} " + "\n")
        output_file.write("------------------" + "\n")
        


