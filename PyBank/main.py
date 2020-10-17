#import OS and CSV
import os
import csv

#Path to collect Data from the Resources folder
budget_data = os.path.join('Resources', 'budget_data.csv')

#Open and read the CSV File
with open(budget_data) as csvfile:
    #Split data on commas
    csvreader = csv.reader(csvfile, delimiter = ',')
    #create variable for counting the number of Months in the dataset
    months_count = 0
    
    #Create a variable for net profit/loss
    net_profit = 0
    
    #create a list for storing the profit differences
    running_profit = 0
    
    #Skip header row
    csv_header = next(csvreader, None)

    #Perform actions on each row
    for row in csvreader:
        months_count += 1
        net_profit += row[1]
        running_profit += row[1]

    average_change = running_profit / (months_count - 1)
    
    print(months_count)
    print(net_profit)
    print(average_change)
