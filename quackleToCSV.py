'''
quackleToCSV.py
By Kevin McElwee

This script runs through the four directories of quackle files -- Traditional,
Lewis, One, and Fifty -- and creates four CSVs with their data parsed from 
parseQuackle. It also appends the percent difference.
'''

import csv
import os
import parseQuackle

for directory in ['traditional', 'lewis', 'one', 'fifty']:
    print("Creating CSV from the games in folder /" + directory + "...")

    testResults = []
    for filename in os.listdir(directory):
        if (filename.endswith('.gcg')):
            file = os.path.join(directory, filename)
            testResults.append(parseQuackle.parseFile(file))                

    with open(directory + '.csv', 'w') as csvfile:
        csvWriter = csv.writer(csvfile, delimiter=',')
        csvWriter.writerow(['file', 's1', 's2', 'b1', 'b2', 'percDif'])

        for r in testResults:
            # 1, 2 index the scores
            percDif = abs(r[1]-r[2]) / ((r[1]+r[2]) / 2) * 100
            csvWriter.writerow(r + [percDif]) 

    print(directory + '.csv is complete')
