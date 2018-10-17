'''
parseQuackle.py
By Kevin McElwee

parseFile: Input gcg file. Returns filename, score1, score2, bingo1, bingo2
isFinishedGame: Checks to make sure that the Quackle games have finished.
'''

def _playerScore(sGame, player1, player2):
    s1, s2 = None, None
    for line in sGame:
        if line.startswith('>'+player1):
            s1 = line
        if line.startswith('>'+player2):
            s2 = line
    # final scores are in the last position
    return int(s1.split(' ')[-1]), int(s2.split(' ')[-1])

def _playerBingo(sGame, player1, player2):
    bingo1, bingo2 = 0, 0
    for line in sGame:
        # The play is indexed at 3 in form 'HEL.O'. Periods are existing tiles
        # if the number of played tiles (not periods) is 7, then it's a bingo
        if len([ch for ch in line.split(' ')[3] if ch != '.']) == 7:
            if line.startswith('>'+player1):
                bingo1 += 1 
            if line.startswith('>'+player2):
                bingo2 += 1
    return bingo1, bingo2

def parseFile(file):
    '''Input gcg file. Return filename, score1, score2, bingo1, bingo2'''
    with open(file) as f:
        player1 = f.readline().split(' ')[1]
        player2 = f.readline().split(' ')[1]
        s = f.readlines()

        if not isFinishedGame(s):
            raise AttributeError(
                f.name + " is unfinished! Use deleteBadFiles.py to "
                "remove unwanted files from your dataset."
            )

        score1, score2 = _playerScore(s, player1, player2)
        bingo1, bingo2 = _playerBingo(s, player1, player2)
    return [f.name, score1, score2, bingo1, bingo2]

def isFinishedGame(sGame):
    return not any([line.startswith('#rack') for line in sGame])

def main():
    filenames = ['test1.gcg', 'test2.gcg', 'test3.gcg']
    directory = 'testGames/'
    testResults = []
    for filename in filenames:
        testResults.append(parseFile(directory + filename))

    with open(directory + 'testAnswers.txt') as file:
        print('COLUMNS:\t' + file.readline(), end='')
        for result in testResults:
            print('TEST RESULTS:\t', end='')
            [print(''.join(str(item)), end=' ') for item in result]
            print('\nANSWERS:\t', file.readline(), end='')

if __name__ == '__main__':
    main()
