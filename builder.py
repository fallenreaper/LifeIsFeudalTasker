#!/bin/python3
import time
from pynput import mouse as MouseListener
from pynput.mouse import Button
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyController
from pynput.keyboard import Key

# tuple of x,y coords.
four_buttons = []
mouse = MouseController()
keyboard = KeyController()

def main():
	print("We need 4 Clicks")
	start_recording()

def on_click(x,y,button,pressed):
	global four_buttons
	if pressed:
		four_buttons.append((x,y))
		if len(four_buttons) == 4:
			stop_recording()

def start_recording():
	with MouseListener.Listener(on_click=on_click) as listener:
		listener.join()

def stop_recording():
	MouseListener.Listener.stop
	while True:
		run_four_buttons()

def run_four_buttons():
	global four_buttons
	print("in Run Four Buttons")
	#click
	mouse.press(Button.left)
	mouse.release(Button.left)
	#shift down
	with keyboard.pressed(Key.shift):	
		#mouse down on 0
		mouse.position = four_buttons[0]
		mouse.press(Button.left)
		#mouse up on 1
		time.sleep(0.5)
		mouse.position = four_buttons[1]
		mouse.release(Button.left)
	#press ok
	time.sleep(0.5)
	mouse.position = four_buttons[2]
	mouse.press(Button.left)
	mouse.release(Button.left)
	#press add resources
	time.sleep(0.5)
	mouse.position = four_buttons[3]
	mouse.press(Button.left)
	mouse.release(Button.left)
	time.sleep(11)

if __name__ == "__main__":
	main()
