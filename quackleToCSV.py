import csv
import os
import parseQuackle

for directory in ['Traditional', 'Lewis', 'One', 'Fifty']:
    print("Creating CSV from the games in folder /" + directory + "...")

    testResults = []
    for filename in os.listdir(directory):
        if (filename.endswith('.gcg')):
            with open(os.path.join(directory, filename)) as file:
                testResults.append(parseQuackle.parseFile(file))

    with open(directory + '.csv', 'w') as csvfile:
        csvWriter = csv.writer(csvfile, delimiter=',')
        csvWriter.writerow(['file', 's1', 's2', 'b1', 'b2', 'percDif'])

        for r in testResults:
            # 1, 2 index the scores
            percDif = abs(r[1]-r[2]) / ((r[1]+r[2]) / 2) * 100
            csvWriter.writerow(r + [percDif]) 

    print(directory + '.csv is complete')