<<<<<<< HEAD
=======
"""
This script is designed to help analyze poll data and show the winner of the election.

Final results will return:
Total votes 
Number of votes for each candidate (and percentage)
Winner of the election

"""

>>>>>>> 217dea807660b2d9fd7e459faa371477ea66b807
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
<<<<<<< HEAD
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
        


=======
    next(csvreader)
    popular_vote = 0 

    # create for loop to iterate each row 
    for row in csvreader:

        # append first row as voter ID
        voter_ID.append(row[0])

        # count the number of voters 
        voter_count = int(len(voter_ID))

        if row[2] == "Khan":
            Khan_count.append(row[2])
            Khan_votes = int(len(Khan_count))
            Khan_percentage = round((Khan_votes / voter_count * 100), 3)

        elif row[2] == "Correy":
            Correy_count.append(row[2])
            Correy_votes = int(len(Correy_count))
            Correy_percentage = round((Correy_votes / voter_count * 100), 3)

        elif row[2] == "Li":
            Li_count.append(row[2])
            Li_votes = int(len(Li_count))
            Li_percentage = round((Li_votes / voter_count * 100), 3)

        elif row[2] == "O'Tooley": 
            OTooley_count.append(row[2])
            OTooley_votes = int(len(OTooley_count))
            OTooley_percentage = round((OTooley_votes / voter_count * 100), 3)

    # set conditions to determine winner 
    if OTooley_percentage > Khan_percentage and OTooley_percentage > Correy_percentage and OTooley_percentage > Li_percentage: 
        winner = "O'Tooley"

    if Khan_percentage > OTooley_percentage and Khan_percentage > Correy_percentage and Khan_percentage > Li_percentage:
        winner = "Khan"

    if Li_percentage > OTooley_percentage and Li_percentage > Khan_percentage and Li_percentage > Correy_percentage: 
        winner = "Li"


# write results in txt file and print in terminal
with open("output.txt", "w") as output_file:

    output_file.write("Election Results" + "\n")
    print("Election Results")
    output_file.write("------------------" + "\n")
    print("------------------")
    output_file.write(f"Total votes: {voter_count}" + "\n")
    print(f"Total votes: {voter_count}")
    output_file.write("------------------" + "\n")
    print("------------------")
    output_file.write(f"Khan: {Khan_percentage}% ({Khan_votes})" + "\n")
    print(f"Khan: {Khan_percentage}% ({Khan_votes})")
    output_file.write(f"Correy: {Correy_percentage}% ({Correy_votes})" + "\n")
    print(f"Correy: {Correy_percentage}% ({Correy_votes})")
    output_file.write(f"Li: {Li_percentage}% ({Li_votes})" + "\n")
    print(f"Li: {Li_percentage}% ({Li_votes})")
    output_file.write(f"O'Tooley: {OTooley_percentage}% ({OTooley_votes})" + "\n")
    print(f"O'Tooley: {OTooley_percentage}% ({OTooley_votes})")
    output_file.write("------------------" + "\n")
    print("------------------")
    output_file.write(f"Winner : {winner} " + "\n")
    print(f"Winner : {winner} ")
    output_file.write("------------------" + "\n")
    print("------------------")
>>>>>>> 217dea807660b2d9fd7e459faa371477ea66b807
