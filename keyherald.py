#Keyherald:Python 2
#Script detect the keypress & sends the keystroke to all the open Image Viewer windows
#Currently relies on the file extension
#Dependencies: Python Keyboard, Xdotool
#Author: Abhishek Munagekar 

import keyboard
import commands
import os
print "Script Launched"


#Detect the multiple shotwell windows open
iv_wins = commands.getstatusoutput('xdotool search --title ".png"')[1].split('\n')[1:]

#.split('\n')[1:]


def send_keypress(key):
	cur_window = commands.getstatusoutput('xdotool getwindowfocus')[1]
	print "Current Window :",cur_window
	for window in iv_wins:
		if window == cur_window:
			continue
		command = 'xdotool windowfocus ' + window
		print command
		os.system(command)
		command = 'xdotool key '+key 
		print command
		os.system(command)



keyboard.add_hotkey('right', send_keypress, args=['Right'], suppress=False, trigger_on_release=True)
keyboard.add_hotkey('left', send_keypress, args=['Left'], suppress=False, trigger_on_release=True)

while True:
	'''
	if keyboard.is_pressed('right'):
		print("Detected right key pressed")
	if keyboard.is_pressed('left'):
		print ("Detecte left key pressed")
		'''