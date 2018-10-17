# scrabble

This project parses data from Quackle, an automated Scrabble player. The results calculate the percent difference for the program playing against itself for various tile values, detailed below. It also identifies bingos, and prints stats concerning how bingo might affect the percent difference.

[Click here for the results](results.csv)

## Getting Started
Python 3
Libraries: pyautogui, scipy, numpy, pandas

After downloading, you should be able to just run `python results.py`, and the calculations should be spat out. If, however, you would like to add games to the directories, please run deleteBadFiles.py, then quackleToCSV.py, then results.py.

## Docstrings ##
#### parseQuackle.py ####
parseFile: Input gcg file. Returns filename, score1, score2, bingo1, bingo2
isFinishedGame: Checks to make sure that the Quackle games have finished.

#### automateQuackle.py ####

This script is a risky, bootstrap way of running multiple Quackle games. The program takes over the keyboard, and manually enters what would be required of a person. The rate is approximately 800 games per hour.

To begin a test, save one file into the desired folder (do not save as [someNumber].gcg). This will set the correct destination for all future games. Then, start one more AI/AI game, begin the program, and quickly return to Quackle. The program should then run smoothly.

Preferably save to an empty folder. As the destination folder gets larger, Quackle 
may take longer than the allotted time to open the save menu. This would throw
everything out of sync, and waste your time.

The process is usually reliable in 1000 interval spurts, and it may be helpful
to disconnect your computer from the internet and close all applications. Sometimes the game is saved before it finishes. See deleteBadFiles.py to help correct these errors.

This is written for Mac (e.g. keyDown('command')).

Reminder: This program takes *ENTIRE CONTROL* of your laptop. Use with caution.

If you find a better way, I'd be happy to hear from you!

#### deleteBadFiles.py ####
Because we automate Quackle hoping that the timing is correct, some files are saved before the game is over. This program searches for "#rack", a string used gcg files to show Quackle where the game was left off.

A list of the error files are printed, and the program offers to delete those files. On average, automateQuackle.py produces incomplete files 1/500 times.

#### quackleToCSV.py ####
This script runs through the four directories of quackle files -- Traditional, Lewis, One, and Fifty -- and creates  CSVs with their data parsed from parseQuackle.py. It also appends the percent difference.

#### results.py ####
Draws data from respective CSVs and prints various tests.
Here are the definitions of the shorthand used.

* avg1st: The average score of the player who went first.
* avg2nd: The average score of the player who went second.
* percDif: The average percent differences between the two scores.
* percDifBingoEquals: The average percent differences between the two scores when both players earned an equal number of bingos.
* percDifBingoUnequal: The average percent differences between the two scores when both players earned an unequal number of bingos.
* avgBingoDif: The average difference in the number of bingos won by each player
* percWinner1st: The percent of games won by the player who went first.
* percWinner1stBingoEqual: The percent of games won by the player who first when the bingos won by each player were equal
* percWinner1stBingoUnequal: The percent of games won by the player who first when the bingos won by each player were unequal
* percBingoEqual: The percent of games where both players had an equal number of bingos
* avgBingoDif: The average difference between the number of bingos  

## Details

There are different size samples, but results.py considers size of sample when calculating mean confidence interval. We could make them the same length, but might as well consider as many datapoints as possible. Make sure to keep this in mind if running different tests. 

All games are calculated with TWL06, the same as Lewis uses in his value

LEWIS
Games within the lewis/ directory were calculated with these tile values
A: 1  B: 3  C: 2  D: 2  E: 1  F: 3  G: 3  H: 2  I: 1  J: 6  K: 4  L: 2  M: 2
N: 1  O: 1  P: 2  Q: 10 R: 1  S: 1  T: 1  U: 2  V: 5  W: 4  X: 5  Y: 3  Z: 6

TRADITIONAL
Games within the traditional/ directory were calculated with these tile values
A: 1  B: 3  C: 3  D: 2  E: 1  F: 4  G: 2  H: 4  I: 1  J: 8  K: 5  L: 1  M: 3
N: 1  O: 1  P: 3  Q: 10 R: 1  S: 1  T: 1  U: 1  V: 4  W: 4  X: 8  Y: 4  Z: 10

ONE, FIFTY
Games within the one/ and fifty/ directories were calculated with all tiles equaling their respective names.
