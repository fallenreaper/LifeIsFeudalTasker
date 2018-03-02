
# POC: William Francis

import datetime
from pynput import keyboard
from pynput import mouse
from pynput.mouse import Button

DEBUG = True
data = {}

def banner():
	print("""
--------------------
| Information:
|
--------------------
""")



def debug(string):
	if DEBUG:
		print(str(string))

def on_click(x, y, button, pressed):	
	if button is Button.left:
		if pressed:
			data["start"] = datetime.datetime.now()
		elif not pressed and "start" in data:
			data["time"] = datetime.datetime.now() - data["start"]
			date["time"] = date["time"].total_seconds() * 1000.0
		debug(data)

def start_recording():
	with mouse.Listener(on_click=on_click) as listener:
		listener.join()

def stop_recording():
	mouse.Listener.stop	

def on_keypress(key):
	try:
		debug(key)
		if key.char is "q" or key.char is "x":
			print("Quitting.")
			return False
		if key.char is "r":
			debug("STARTING RECORDING")
			start_recording()
		if key.char is "s":
			debug("STOPPING RECORDING")
			stop_recording()
	except AttributeError as e:
		print("Error %s " % str(e))

def keyup(key):
	pass

with keyboard.Listener(on_press=on_keypress, on_release=keyup) as listener:
	listener.join()		
