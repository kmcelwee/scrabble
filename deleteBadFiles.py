'''
Because we automate Quackle hoping that the timing is correct, some files are
saved before the game is over. This program searches for "#rack", a string used
in unfinished games to show Quackle where the game was left off.

A list of the error files are printed.
'''

import os
import parseQuackle

directories = ['Traditional', 'Lewis', 'One', 'Fifty']

for directory in directories:
	print('Looking for unfinished games in directory /' + directory + "...")

	errorFiles = []
	for filename in os.listdir(directory):
		if (filename.endswith(".gcg")):
			file = os.path.join(directory, filename)
			with open(file) as f:
				if not parseQuackle.isFinishedGame(f):
					errorFiles.append(file)

	if len(errorFiles) == 0:
		print("All good! No unfinished games found")
	else:
		print("ERROR FILES")
		for errorFile in errorFiles:
			print(errorFile)
		if input("Delete the files above? (Y/N)\n") in ['yes', 'Y', 'y']:
			for errorFile in errorFiles:
				os.unlink(errorFile)
			print("Deletion complete")
		else:
			print("Deletion cancelled")
