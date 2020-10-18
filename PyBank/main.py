#import OS and CSV
import os
import csv

#Path to collect Data from the Resources folder
budget_data = os.path.join('Resources', 'budget_data.csv')

#Open and read the CSV File
with open(budget_data, 'r') as csvfile:
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

    #list for min/max
    max_min_list = []

    #Perform actions on each row
    for row in csvreader:
        months_count += 1
        net_profit += int(row[1])
        
        #average profit changes, add to list
        running_profit_2 = running_profit_1
        running_profit_1 = int(row[1])
        running_profit_difference = running_profit_1 - running_profit_2
        running_profit.append(int(running_profit_difference))

        #append values to max/min list
        max_min_list.append(int(row[1]))

        
#finish up calculating running profit average, remove the first list item, sum all items in the list and divide by number of months    
    running_profit.pop(0)
    running_profit_total = sum(running_profit)    
    average_change = running_profit_total / (months_count - 1)
    average_change = "{:.2f}".format(average_change)

#greatest increase / decrease if statement
    max_profit = max(max_min_list)
    min_profit = min(max_min_list)
   
    max_profit_month = 'unknown'
    min_profit_month = 'unknown'

with open(budget_data, 'r') as csvfile:
    #Split data on commas
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader, None)

    for row in csvreader:
        if int(row[1]) == max_profit:
            max_profit_month  = row[0]
        elif int(row[1]) == min_profit:
            min_profit_month = row[0]
    
print('')    
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {months_count}')
print(f'Total: ${net_profit}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {max_profit_month} (${max_profit})')
print(f'Greatest Decrease in Profits: {min_profit_month} (${min_profit})')
print('') 


f = open("PyBank.txt", "w+")
f.write(''+ '\n')
f.write('Financial Analysis'+ '\n')
f.write('----------------------------'+ '\n')
f.write(f'Total Months: {months_count}'+ '\n')
f.write(f'Total: ${net_profit}'+ '\n')
f.write(f'Average Change: ${average_change}'+ '\n')
f.write(f'Greatest Increase in Profits: {max_profit_month} (${max_profit})'+ '\n')
f.write(f'Greatest Decrease in Profits: {min_profit_month} (${min_profit})'+ '\n')
f.write(''+ '\n') 
f.close()