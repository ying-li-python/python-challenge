# This script is designed to help analyze financial records
# For instance, calculations for total profit for the period, total months, average change, 
# and the month that showed greatest increase or decrease of profits 


# import dependencies 
import os
import csv

# add variable to the CSV file 
bankCSV = os.path.join(os.path.dirname(__file__), 'Resources', 'budget_data.csv')

# set output path 
output_path = os.path.join("output.csv")


# create empty lists for calculating total months, net profit/losses
date = []
net_profit = []

# open backCSV as csvfile using csvreader
with open(bankCSV, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header 

    next(csvreader)

    # set values for calculating max and min profit 
    max_profit = 0 
    min_profit = 0

    # create for loop  
    for row in csvreader: 
        
        # calculate the total number of months from column 1
        date.append(row[0])
        month_count = len(date)
        month_total = 0
        month_total += month_count

        # for calculating net profit/loss, append each row of profit to net_profit list
        net_profit.append(int(row[1]))

        # create variable to store total net profit/loss, starting at 0
        total_net_profit = 0

        # calculate net profit/losses from net_profit list
        for data in net_profit: 
            total_net_profit += data 

        # create conditionals for calculating average change 
        
        if (row[0] == "Jan-2010"): # start of the period 
            start_month = int(row[1])    


        if (row[0] == "Feb-2017"): # end of the period
            end_month = int(row[1])     

        # set conditionals for grabbing the maximum and minimum profit 
        if (int(row[1]) >= int(max_profit)):
            max_profit = row[1]
            date_max = row[0]

        if (int(row[1]) <= int(min_profit)):
            min_profit = row[1]
            date_min = row[0]
        
    # solution for average change, with round() function to include up to two decmials
    average_change = round((end_month - start_month)/(month_total-1), 2)

    # Print out the results in terminal

    print("Financial Analysis")
    print("------------------")
    print(f'Total Months: {month_total}')
    print(f'Total: ${total_net_profit}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {date_max} (${max_profit})')
    print(f'Greatest Decrease in Profits: {date_min} (${min_profit})')

# write results in new csv file 
with open(output_path, 'w', newline='') as resultsfile:

    # Initialize csv.writer
    writer = csv.writer(resultsfile)

    # write titles in header 
    writer.writerow(["Total Months", "Total($)", "Average Change ($)", "Greatest Increase in Profits (date)",
    "Amount ($)", "Greatest Decrease in Profits (date)", "Amount ($)"]) 

    # write results 
    writer.writerow([str(month_total), str(total_net_profit), str(average_change), str(date_max), str(max_profit), 
    str(date_min), str(min_profit)])
