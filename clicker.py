
# POC: William Francis

from pynput.mouse import Button, Controller
import time

mouse = Controller()
x = 0

while True:
	x+=1
	print("Left Mouse Tap")
	mouse.press(Button.left)
	mouse.release(Button.left)
	time.sleep(3)
	if x >= 5:
		exit(0)
