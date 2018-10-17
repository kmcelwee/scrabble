'''

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
	