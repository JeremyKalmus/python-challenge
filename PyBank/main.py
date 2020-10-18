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
    running_profit =[]
    running_profit_difference = 0
    running_profit_1 = 0
    running_profit_2 = 0
    #Skip header row
    csv_header = next(csvreader, None)

    #Perform actions on each row
    for row in csvreader:
        months_count += 1
        net_profit += int(row[1])
        
        #average profit changes, add to list
        running_profit_2 = running_profit_1
        running_profit_1 = int(row[1])
        running_profit_difference = running_profit_1 - running_profit_2
        running_profit.append(int(running_profit_difference))

#finish up calculating running profit average, remove the first list item, sum all items in the list and divide by number of months    
    running_profit.pop(0)
    running_profit_total = sum(running_profit)    
    average_change = running_profit_total / (months_count - 1)

#greatest increase / decrease if statement
    max_profit = int(max(running_profit))
    min_profit = int(min(running_profit))
    value = row[1]
    max_profit_month = 'unknown'
    min_profit_month = 'unknown'

    for row in csvreader: 
        if value == max_profit:
            max_profit_month = row[0]
        elif value == min_profit:
            min_profit_month = row[0]
    
    print(months_count)
    print(net_profit)
    print(average_change)
    print(max_profit_month)
    print(min_profit_month)
