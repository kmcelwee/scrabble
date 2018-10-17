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
    'avg1st': {}, 'avg2nd': {}, 'percDif': {}, 'percDifBingoEquals': {},
    'percDifBingoUnequal': {}, 'avgBingoDif': {},
    'percWinner1st': {}, 'percWinner1stBingoEqual': {}, 'percWinner1stBingoUnequal':{},
    'percBingoEqual': {},
}

directories = ['traditional', 'Lewis', 'One', 'Fifty']

for d in directories:
    with open(d + '.csv') as csv_file:
        f = csv.DictReader(csv_file, delimiter=',')
        score1, score2 = [], []
        bingo1, bingo2 = [], []
        bingoEqual, bingoUnequal = [], []
        winner1stBingoEqual, winner1stBingoUnequal = [],[]

        for row in f:
            score1.append(int(row['s1']))
            score2.append(int(row['s2']))
            bingo1.append(int(row['b1']))
            bingo2.append(int(row['b2']))
            if row['b1'] == row['b2']:
                bingoEqual.append(float(row['percDif']))
                if int(row['s1'] > row['s2']):
                    winner1stBingoEqual.append(float(row['percDif']))
            else:
                bingoUnequal.append(float(row['percDif']))
                if int(row['s1'] > row['s2']):
                    winner1stBingoUnequal.append(float(row['percDif']))

        totalRows = len(score1)
        assert len(score1) == len(score2)
        assert len(bingoEqual) + len(bingoUnequal) == len(score1)

        tests['avg1st'][d] = meanAndConf(score1)
        tests['avg2nd'][d] = meanAndConf(score2)
        tests['percDifBingoEquals'][d] = meanAndConf(bingoEqual) + '%'
        tests['percDifBingoUnequal'][d] = meanAndConf(bingoUnequal) + '%'
        tests['percDif'][d] = meanAndConf(bingoUnequal + bingoEqual) + '%'

        bingoDif = [abs(b1 - b2) for b1, b2 in zip(bingo1, bingo2)]
        tests['avgBingoDif'][d] = meanAndConf(bingoDif)

        tests['percBingoEqual'][d] = len(bingoEqual) / totalRows * 100

        winner1st = [1 for (s1, s2) in zip(score1, score2) if s1 > s2]
        tests['percWinner1st'][d] = len(winner1st) / totalRows * 100

        bingoDif = [abs(b1 - b2) for b1, b2 in zip(bingo1, bingo2)]
        tests['avgBingoDif'][d] = meanAndConf(bingoDif)
        
        tests['percWinner1stBingoEqual'][d] = len(winner1stBingoEqual) / len(bingoEqual) * 100
        tests['percWinner1stBingoUnequal'][d] = len(winner1stBingoUnequal) / (totalRows - len(bingoEqual)) * 100

with open('quackleData.csv', 'w') as csvfile:
    csvWriter = csv.writer(csvfile)
    csvWriter.writerow(['test'] + directories)
    for test in tests:
        csvWriter.writerow([test] + list(tests[test].values()))

df = pandas.read_csv('quackleData.csv')
print(df)

