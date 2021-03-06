"""
This script is designed to help convert employee records to the required format. 

"Full name" is split into "First Name" and "Last Name"
Birthdate (YYYY-MM-DD) is converted to MM/DD/YYYY 
9-digit SSN is converted to hide the first 5 numbers of the SSN with an asterisk (*)
States are converted to their abbreviations (California -> CA)


Example: $ python main.py

"""
# import dependencies 
import os
import csv

# add variable to the CSV file 
employeeCSV = os.path.join(os.path.dirname(__file__),'employee_data.csv')

# set output path 
output_path = os.path.join("output.csv")


# create empty lists 
employeeID = []
first_name_final = []
last_name_final = []
birthDate = []
corrected_birthDate = []
socialsecurity_data = []
final_SSN = []
state = []
revised_states = []

# open employeeCSV as csvfile using csvreader
with open(employeeCSV, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header 
    next(csvreader)


    # dictionary of US state abbreviations 
    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    }

    # create for loop to clean data
    for row in csvreader:
     
        # create list of employee IDs for each employee
        employeeID.append(row[0])

        # split Name into First and Last Name of each employee
        first_name = row[1].split()[0]
        last_name = row[1].split()[1]

        # append first and last name to list
        first_name_final.append(first_name)
        last_name_final.append(last_name)

        # create list of date of birth of each employee
        birthDate.append(row[2])

        # for loop to convert birthDate to MM/DD/YY format
        for dates in birthDate:
            revised_birthDate = '/'.join(reversed(dates.split('-')))
            # result: DD/MM/YYYY

            for i in revised_birthDate: 
                month = revised_birthDate[3:6]
                day = revised_birthDate[0:3]
                year = revised_birthDate[6:12]
                
                final_date = month + day + year

        corrected_birthDate.append(final_date)


        # create list of SSN of each empolyee
        socialsecurity_data.append(row[3])

        # for loop to convert SSN to hide first five numbers with *
        for numbers in socialsecurity_data: 
            for i in numbers:
                firstFive = numbers[0:6]
                firstFive = firstFive.replace(numbers[0:6], "***-**")
                lastFive = numbers[6:11]
                result_SSN = firstFive + lastFive
        final_SSN.append(result_SSN)
        
        # create list of state location of each employee
        state.append(row[4])

        # for loop to convert state names to abbreviations 
        for name in state: 
            for statename, value in us_state_abbrev.items():
                if name == statename: 
                    renamed_state = value
        revised_states.append(renamed_state)

# assign a variable to cleaned lists 
employee_cleaned = zip(employeeID, first_name_final, last_name_final, corrected_birthDate, final_SSN, revised_states)

# write results to new csv file 
with open('output.csv', 'w', newline='') as resultsfile:

    # initialize csv writer
    writer = csv.writer(resultsfile)

    # create header row with titles
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    # add data to rows 
    writer.writerows(employee_cleaned)
