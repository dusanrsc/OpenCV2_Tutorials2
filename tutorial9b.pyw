# importing modules
import cv2
import numpy

# function for clicking
def click_event(event, x, y, flags, parameters):
	# on left mouse button down
	if event == cv2.EVENT_LBUTTONDOWN:
		# instantces of colors with color chanels
		blue = resized_img[x, y, 0]
		green = resized_img[x, y, 1]
		red = resized_img[x, y, 2]

		# draw circle
		cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

		# draw black image
		color_img = numpy.zeros((256, 256, 3), numpy.uint8)

		# fill "black" img with picked color from main image
		# this works like bgr color picker
		color_img[:] = [blue, green, red]
		
		# displaying img
		# creating new window with new picked color
		cv2.imshow("Color", color_img)

# creating black img with numpy
#img = numpy.zeros((512, 512, 3), numpy.uint8)

# loading img
img = cv2.imread("assets/soccer_practice.jpg")

# this wasnt on the tutorial but image is to large
# processing image (resizing)
resized_img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# displaying img
cv2.imshow("Tutorial9B", resized_img)

# creating empty list variable
points = []

# setting mouse callback when is clicked
cv2.setMouseCallback("Tutorial9B", click_event)

# not allowing window to close
cv2.waitKey(0)

# destroying all windows
cv2.destroyAllWindows()