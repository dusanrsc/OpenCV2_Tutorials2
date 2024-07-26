# importing modules
import cv2
import numpy

# function for tracking trackbar value/x position
def nothing(x):
	return None

# variable section
switch = "CHANNEL"

# creating actual window for setting trackbars on it
cv2.namedWindow("Tutorial12B")

# creating GUI trackbar (slider kind of stuff)
# createTrackbar("TrackbarName", "windowName", minValue, maxValue, function)
cv2.createTrackbar("POSITION", "Tutorial12B", 0, 100, nothing)
cv2.createTrackbar(switch, "Tutorial12B", 0, 1, nothing)

# main loop
while True:
	# reading image
	img = cv2.imread("assets/ronaldo.jpg")

	# tracking trackbar values
	pos = cv2.getTrackbarPos("POSITION", "Tutorial12B")

	# font instance
	font = cv2.FONT_HERSHEY_SIMPLEX

	# displaying text on the image
	cv2.putText(img, str(pos), (10, 40), font, 1, (0, 255, 0), 2)

	# setting event/key setter
	key = cv2.waitKey(1) & 0xFF

	# event is q key break
	if key == ord("q"):
		break

	# get track of switch channel trackbar
	switch_get = cv2.getTrackbarPos(switch, "Tutorial12B")

	# change color channel by conditioning
	if switch_get == 0:
		pass
	else:
		img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# displaying current image
	img = cv2.imshow("Tutorial12B", img)

# destroying all windows
cv2.destroyAllWindows()