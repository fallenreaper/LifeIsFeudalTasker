#!/bin/python3

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class PynputMouseClick:
	def __init__(self, x, y, button, pressed):
		self.point = Point(x,y)
		self.button = button
		self.pressed = pressed

class EventNode:
	def __init__(self, cursor=None):
		self.cursor = cursor
	

class MyMouseEvent(EventNode):
	def __init__(self, cursor=None, mouse=None):
		EventNode.__init__(self, cursor)
		self.mouse = mouse

class MyKeyboardEvent(EventNode):
	def __init__(self, cursor=None, key=None):
		EventNode.__init__(self, cursor)
		self.key = key
