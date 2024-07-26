# importing modules
import cv2
import numpy

# function for tracking trackbar value/x position
def nothing(x):
	return None

# creating black image
img = numpy.zeros((300, 512, 3), numpy.uint8)

# creating actual window for setting trackbars on it
cv2.namedWindow("Tutorial12A")

# creating GUI trackbar (slider kind of stuff)
# to handle color changing createTrackbar("TrackbarName", "windowName", minValue, maxValue, function)
cv2.createTrackbar("BLUE", "Tutorial12A", 0, 255, nothing)
cv2.createTrackbar("GREEN", "Tutorial12A", 0, 255, nothing)
cv2.createTrackbar("RED", "Tutorial12A", 0, 255, nothing)

# main loop
while True:
	# displaying image
	cv2.imshow("Tutorial12A", img)

	# setting event/key setter
	key = cv2.waitKey(1) & 0xFF

	# event is q key break
	if key == ord("q"):
		break

	# get all trackbars value for each color chanel
	b = cv2.getTrackbarPos("BLUE", "Tutorial12A")
	g = cv2.getTrackbarPos("GREEN", "Tutorial12A")
	r = cv2.getTrackbarPos("RED", "Tutorial12A")

	img[:] = [b, g, r]

# destroying all windows
cv2.destroyAllWindows()