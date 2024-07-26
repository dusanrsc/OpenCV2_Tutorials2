# importing modules
import cv2
import numpy

# looping through classes and functions in cv2 library and filtering it by condition
#events = [i for i in dir(cv2) if "EVENT" in i]

# printing filtered events
#print(events)

# function for clicking
def click_event(event, x, y, flags, parameters):
	# on left mouse button down
	if event == cv2.EVENT_LBUTTONDOWN:
		# font instance
		font = cv2.FONT_HERSHEY_SIMPLEX

		# drawing text on the img with x and y coords
		cv2.putText(resized_img, f"{x}, {y}", (x, y), font, 0.5, (0, 255, 0), 2)

		# displaying current img with x and y coords
		cv2.imshow("Tutorial8", resized_img)

	# on right mouse button down
	if event == cv2.EVENT_RBUTTONDOWN:
		# instantces of colors with color chanels
		blue = resized_img[y, x, 0]
		green = resized_img[y, x, 1]
		red = resized_img[y, x, 2]

		# font instance
		font = cv2.FONT_HERSHEY_SIMPLEX

		# drawing text on the img with bgr color value
		cv2.putText(resized_img, f"{blue}, {green}, {red}", (x, y), font, 0.5, (255, 255, 0), 2)

		# displaying current img with bgr color value
		cv2.imshow("Tutorial8", resized_img)

# creating black img with numpy
#img = numpy.zeros((512, 512, 3), numpy.uint8)

# loading img
img = cv2.imread("assets/soccer_practice.jpg")

# this wasnt on the tutorial but image is to large
# processing image (resizing)
resized_img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# displaying img
cv2.imshow("Tutorial8", resized_img)

# setting mouse callback when is clicked
cv2.setMouseCallback("Tutorial8", click_event)

# not allowing window to close
cv2.waitKey(0)

# destroying all windows
cv2.destroyAllWindows()
