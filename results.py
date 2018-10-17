'''
results.py
By Kevin McElwee

Draws data from respective CSVs and prints various tests.
Here are the definitions of the shorthand used.

* avg1st: The average score of the player who went first.
* avg2nd: The average score of the player who went second.
* percDif: The average percent differences between the two scores.
* percDifBingoEquals: The average percent differences between the two scores 
    when both players earned an equal number of bingos.
* percDifBingoUnequal: The average percent differences between the two scores 
    when both players earned an unequal number of bingos.
* avgBingoDif: The average difference in number of bingos won by each player
* percWinner1st: The percent of games won by the player who went first.
* percWinner1stBingoEqual: The percent of games won by the player who first 
    when the bingos won by each player were equal
* percWinner1stBingoUnequal: The percent of games won by the player who 
    first when the bingos won by each player were unequal
* percBingoEqual: The percent of games where both players had an equal 
    number of bingos
* avgBingoDif: The average difference between the number of bingos  

'''

import csv
import numpy as np
import pandas
import scipy.stats

def meanAndConf(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return str(round(m, 3)) + " ± " + str(round(h, 1))
    # Rounding was not rigorous.

tests = {
    'avg1st': {}, 'avg2nd': {}, 'percDif': {}, 'percDifBingoEqual': {},
    'percDifBingoUnequal': {}, 'avgBingoDif': {},
    'percWinner1st': {}, 'percWinner1stBingoEqual': {}, 
    'percWinner1stBingoUnequal':{}, 'percBingoEqual': {},
}

directories = ['traditional', 'lewis', 'one', 'fifty']

for d in directories:
    with open(d + '.csv') as csv_file:
        f = csv.DictReader(csv_file, delimiter=',')
        score1, score2 = [], []
        bingo1, bingo2 = [], []
        bEqual, bUnequal = [], []
        w1stBEqu, w1stBUnequ = [],[]

        for row in f:
            score1.append(int(row['s1']))
            score2.append(int(row['s2']))
            bingo1.append(int(row['b1']))
            bingo2.append(int(row['b2']))
            if row['b1'] == row['b2']:
                bEqual.append(float(row['percDif']))
                if int(row['s1'] > row['s2']):
                    w1stBEqu.append(float(row['percDif']))
            else:
                bUnequal.append(float(row['percDif']))
                if int(row['s1'] > row['s2']):
                    w1stBUnequ.append(float(row['percDif']))

        total = len(score1)
        assert len(score1) == len(score2)
        assert len(bEqual) + len(bUnequal) == len(score1)

        tests['avg1st'][d] = meanAndConf(score1)
        tests['avg2nd'][d] = meanAndConf(score2)
        tests['percDifBingoEqual'][d] = meanAndConf(bEqual) + '%'
        tests['percDifBingoUnequal'][d] = meanAndConf(bUnequal) + '%'
        tests['percDif'][d] = meanAndConf(bUnequal + bEqual) + '%'

        bingoDif = [abs(b1 - b2) for b1, b2 in zip(bingo1, bingo2)]
        tests['avgBingoDif'][d] = meanAndConf(bingoDif)

        tests['percBingoEqual'][d] = len(bEqual) / total * 100

        winner1st = [1 for (s1, s2) in zip(score1, score2) if s1 > s2]
        tests['percWinner1st'][d] = len(winner1st) / total * 100

        bingoDif = [abs(b1 - b2) for b1, b2 in zip(bingo1, bingo2)]
        tests['avgBingoDif'][d] = meanAndConf(bingoDif)
        
        tests['percWinner1stBingoEqual'][d] = len(w1stBEqu) / len(bEqual) * 100
        tests['percWinner1stBingoUnequal'][d] = len(w1stBUnequ) / (total-len(bEqual)) * 100

with open('quackleData.csv', 'w') as csvfile:
    csvWriter = csv.writer(csvfile)
    csvWriter.writerow(['test'] + directories)
    for test in tests:
        csvWriter.writerow([test] + list(tests[test].values()))

df = pandas.read_csv('quackleData.csv')
print(df)
