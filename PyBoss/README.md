# PyBoss 

In this data-centric world, we have to mantain old records as we upgrade into newer systems. But, old records have to be converted to an appropriate format to be read by the new system. In this case, let's convert employee records. 

This folder contains the script that for each employee, converts fullnames into first and last name, the 9-digit SSN to hide the first five numbers with an asterisk, location by state to their abbreivations (California -> CA), birthdate to MM/DD/YYYY.

## Resources: 
- Employee data has been kindly provided by UC Berkeley's Data Analytics and Visualization 

## Demonstration 

This csv file needs to be converted to be an appropriate format for HR.  

```
head employee_data.csv 
```
Will show: 

<img src="https://raw.githubusercontent.com/ying-li-python/python-challenge/master/PyBoss/Images/originaldata.png">

For this python script, we used data structures (dictionarys and lists), ```.join()```, ```.split()``` ,and ```.replace()``` functions, created nested for-loops, and used the csv module to write our results. 

To run the script: 
```
cd PyBoss
python main.py 
```
Running this script will generate an output csv file in the same folder. You're done! 

Let's check our results.

```
head output.csv 
```
Will show: 

<img src="https://raw.githubusercontent.com/ying-li-python/python-challenge/master/PyBoss/Images/output.png">

