'''
automateQuackle.py
by Kevin McElwee

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
'''

from time import sleep
import pyautogui as p

i = 0

while (i < 3000):
	# Typical time for a computer to run against itself
	sleep(2.5)

	# New Quackle Game
	p.keyDown('command')
	sleep(0.05)
	p.typewrite(['n'])
	sleep(0.05)
	p.keyUp('command')

	sleep(0.1)

	# Would you like to save game? Yes (enter)
	p.typewrite(['enter'])

	# It takes a surprisingly long time to open the save menu
	sleep(1.75)

	# Save as the number
	p.typewrite(str(i))
	sleep(0.1)
	p.typewrite(['enter'])

	# New game screen, "Speedy Player" v. "Speedy Player", yes (enter)
	sleep(0.1)
	p.typewrite(['enter'])

	i += 1
	