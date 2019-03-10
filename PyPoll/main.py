# import dependencies
import os
import csv

pollCSV = os.path.join(os.path.dirname(__file__), 'Resources', 'election_data.csv')

# set output path

output_path = os.path.join("output.csv")

# create empty lists for voter_ID, candidate total, and for each candidate
voter_ID = []
candidate = []
Khan_count = []
Correy_count =[]
Li_count =[]
OTooley_count = []


with open(pollCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header
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
    if OTooley_percentage > Khan_percentage and OTooley_percentage > Correy_percentage and OTooley_count > Li_percentage: 
        winner = "O'Tooley"

    if Khan_percentage > OTooley_percentage and Khan_percentage > Correy_percentage and Khan_percentage > Li_percentage:
        winner = "Khan"

    if Li_percentage > OTooley_percentage and Li_percentage > Khan_percentage and Li_percentage > Correy_percentage: 
        winner = "Li"


    # print results
    print("Election Results")
    print("------------------")
    print(f"Total votes: {voter_count}")
    print("------------------")
    print(f"Khan: {Khan_percentage}% ({Khan_votes})")
    print(f"Correy: {Correy_percentage}% ({Correy_votes})")
    print(f"Li: {Li_percentage}% ({Li_votes})")
    print(f"O'Tooley: {OTooley_percentage}% ({OTooley_votes})")
    print("------------------")
    print(f"Winner : {winner} ")
    print("------------------")

# write results in new csv file 
with open(output_path, 'w', newline='') as resultsfile:

    # Initialize csv.writer
    writer = csv.writer(resultsfile)

    # write titles in header 
    writer.writerow(["Total Votes", "Khan votes (%)", "Total Khan Votes", "Correy votes (%)",
    "Total Correy Votes", "Li votes (%)", "Total Li Votes", "O'Tooley votes (%)", "Total O'Tooley Votes", "Winner"]) 

    # write results 
    writer.writerow([str(voter_count), str(Khan_percentage), str(Khan_votes), str(Correy_percentage), str(Correy_votes), 
    str(Li_percentage), str(Li_votes), str(OTooley_percentage), str(OTooley_votes), str(winner)])


