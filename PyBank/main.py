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

# create empty lists to store column data
months = []
profits_over_time = []

# open backCSV as csvfile using csvreader
with open(bankCSV, 'r') as csvfile: 
    csvreader = csv.reader(csvfile)
    
    # skip header 
    next(csvreader)

    # create for loop 
    for row in csvreader: 
        
        # add values to list
        months.append(row[0])
        profits_over_time.append(row[1])

        # define variables and set to 0 
        total_profit = 0 
        total_months = 0
        max_profit = 0
        min_profit = 0 

        # create for loop for profit/losses column 
        for profit in profits_over_time:

            # calculate total months 
            total_months = len(profits_over_time) 
        
            # calculate total profit 
            total_profit += int(profit)

            # find open and close amounts by list index 
            open_amount = int(profits_over_time[0])
            close_amount = int(profits_over_time[-1])

            # create conditional to find max profit of the entire period and index for corresponding month/year
            if int(profit) >= int(max_profit):
                max_profit = profit 
                max_postion = profits_over_time.index(max_profit)
                max_month = months[int(max_postion)]

            # create conditional to find min profit of the entire period and index for corresponding month/year
            if int(profit) <= int(min_profit): 
                min_profit = profit
                min_postion = profits_over_time.index(min_profit)
                min_month = months[int(min_postion)]

    # solution to find average change over the entire period         
    average_change = round((close_amount - open_amount)/(total_months-1),2)


# write results in new text file and print results in terminal 
with open("output.txt", "w") as output_file:

    output_file.write("Financial Analysis" + "\n")
    print("Financial Analysis")
    output_file.write("------------------" + "\n")
    print("------------------")
    output_file.write(f'Total Months: {total_months}' + "\n")
    print(f'Total Months: {total_months}')
    output_file.write(f'Total: ${total_profit}'+ "\n")
    print(f'Total: ${total_profit}')
    output_file.write(f'Average Change: ${average_change}' + "\n")
    print(f'Average Change: ${average_change}')
    output_file.write(f'Greatest Increase in Profits: {max_month} (${max_profit})'+ "\n")
    print(f'Greatest Increase in Profits: {max_month} (${max_profit})')
    output_file.write(f'Greatest Decrease in Profits: {min_month} (${min_profit})'+ "\n")
    print(f'Greatest Decrease in Profits: {min_month} (${min_profit})')