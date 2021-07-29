"""
File: sierpinski.py
Name: Charlene
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	Draw Sierpinski triangles with specific order.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	Draw Sierpinski triangles with specific order.

	:param order: an int representing the extent of drawing Sierpinski triangles
	:param length: an int representing the length of the first-order Sierpinski triangle
	:param upper_left_x: an int representing the upper left x coordinate of the first-order Sierpinski triangle
	:param upper_left_y: an int representing the upper left y coordinate of the first-order Sierpinski triangle
	"""
	# Determine base case where the first order Sierpinski triangle is drawn
	if order == 0:
		top = GLine(upper_left_x, upper_left_y, upper_left_x+length, upper_left_y)
		left = GLine(upper_left_x, upper_left_y, upper_left_x+0.5*length, upper_left_y+0.866*length)
		right = GLine(upper_left_x+length, upper_left_y, upper_left_x+0.5*length, upper_left_y+0.866*length)
		window.add(top)
		window.add(left)
		window.add(right)
		# Slow down the process of drawing each triangle for observation
		pause(50)
	# Determine recursive case where this function is called at every corner of Sierpinski triangle ordered previously
	else:
		sierpinski_triangle(order-1, 0.5*length, upper_left_x, upper_left_y)
		sierpinski_triangle(order-1, 0.5*length, upper_left_x+0.5*length, upper_left_y)
		sierpinski_triangle(order-1, 0.5*length, upper_left_x+0.5**2*length, upper_left_y+0.5*0.866*length)


if __name__ == '__main__':
	main()