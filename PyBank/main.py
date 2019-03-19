"""
This script is designed to help analyze financial records. 

Results will return: 
Total profit for the period
Total months 
Average change 
Month that showed greatest increase or decrease of profits 

Example: $ python main.py

"""
# import dependencies 
import os
import csv

# add variable to the CSV file 
bankCSV = os.path.join(os.path.dirname(__file__), 'Resources', 'budget_data.csv')


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


# write results in new text file and print results in terminal 
with open("output.txt", "w") as output_file:

    output_file.write("Financial Analysis" + "\n")
    print("Financial Analysis")
    output_file.write("------------------" + "\n")
    print("------------------")
    output_file.write(f'Total Months: {month_total}' + "\n")
    print(f'Total Months: {month_total}')
    output_file.write(f'Total: ${total_net_profit}'+ "\n")
    print(f'Total: ${total_net_profit}')
    output_file.write(f'Average Change: ${average_change}' + "\n")
    print(f'Average Change: ${average_change}')
    output_file.write(f'Greatest Increase in Profits: {date_max} (${max_profit})'+ "\n")
    print(f'Greatest Increase in Profits: {date_max} (${max_profit})')
    output_file.write(f'Greatest Decrease in Profits: {date_min} (${min_profit})'+ "\n")
    print(f'Greatest Increase in Profits: {date_max} (${max_profit})')
