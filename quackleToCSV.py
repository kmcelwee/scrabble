'''
quackleToCSV.py
By Kevin McElwee

This script runs through the directories of quackle files and creates CSVs 
with their data parsed from parseQuackle. It also appends the percent 
difference.
'''

import csv
import os
import parseQuackle

DATA = 'data/'
directories = [subdir for subdir,_,_ in os.walk(DATA) if subdir != DATA]

for directory in directories:
    print("Creating CSV from the games in folder " + directory + "...")

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
            csvWriter.writerow([os.path.basename(r[0])] + r[1:] + [percDif]) 

    print(directory + '.csv is complete')
