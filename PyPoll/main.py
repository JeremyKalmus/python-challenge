#import OS and CSV
import os
import csv

#Path to collect Data from the Resources folder
election_data = os.path.join('Resources', 'election_data.csv')

#Open file and Read CSV
with open(election_data, 'r') as csvfile:
    #split data on commas
    csvreader = csv.reader(csvfile, delimiter = ',')
    #create a variable to count the number of votes
    votes_cast = 0
    #create canidates list
    canidates = [0,0,0,0]

    #Perform actions on each row
    for row in csvreader:
        votes_cast += 1

        if row[2] == 'Khan':
            canidates[0] += 1
        elif row[2] == 'Correy':
            canidates[1] += 1
        elif row[2] == 'Li':
            canidates[2] += 1
        elif row[2] == "O'Tooley":
            canidates[3] += 1

#variables for canidates for win %
khan = canidates[0] / votes_cast
correy = canidates[1] / votes_cast
li = canidates[2] / votes_cast
o_tooley = canidates[3] / votes_cast

#print results
print('')
print('Election Results')
print('-------------------------')
print("Total Votes: {}".format(votes_cast))
print('-------------------------')
print('Kahn: {:.3%} ({})'.format(khan,canidates[0]))
print('correy: {:.3%} ({})'.format(correy,canidates[1]))
print('Li: {:.3%} ({})'.format(li,canidates[2]))
print("O'Tooley: {:.3%} ({})".format(o_tooley,canidates[3]))
print('-------------------------')
print("Winner: Khan")
print('-------------------------')
print('')

#create txt file and print results
f = open('PyPoll.txt', "w+")
f.write('' + '\n')
f.write('Election Results'+ '\n')
f.write('-------------------------'+ '\n')
f.write("Total Votes: {}".format(votes_cast)+ '\n')
f.write('-------------------------'+ '\n')
f.write('Kahn: {:.3%} ({})'.format(khan,canidates[0])+ '\n')
f.write('correy: {:.3%} ({})'.format(correy,canidates[1])+ '\n')
f.write('Li: {:.3%} ({})'.format(li,canidates[2]))
f.write("O'Tooley: {:.3%} ({})".format(o_tooley,canidates[3])+ '\n')
f.write('-------------------------'+ '\n')
f.write("Winner: Khan"+ '\n')
f.write('-------------------------'+ '\n')
f.write(''+ '\n')


f.close()