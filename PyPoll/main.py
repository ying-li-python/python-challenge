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
        k = names 
        v = candidate_votes.count(names)
        p = round((v / voter_count) * 100, 2) 
        p = "{}%".format(p)
        v = "({})".format(v)
        d[k] = p, v 


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

        for k, v in d.items():
            percentage= str(v[0])
            votes = str(v[1])
            print(str(k) + ": " + str(percentage) + " " + str(votes))  
            winner = max(d, key=lambda k:d[k])
            results = str(k) + ": " + str(percentage) + " " + str(votes) + "\n"
            output_file.write(results)

        print("------------------")
        print("Winner: " + str(winner))
        print("------------------")


        output_file.write("------------------" + "\n")
        output_file.write(f"Winner : {winner} " + "\n")
        output_file.write("------------------" + "\n")
        


