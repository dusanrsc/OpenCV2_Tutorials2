### NOTE: QUICK STEPS FOR DETECTING OBJECTS ARE
# 1) loading image
# 2) converting image
# 3) preparing threshold values
# 4) creating mask 
# 5) bitwise operation
# 6) displaying finall result

# importing modules
import cv2
import numpy

# defining dummy function
def nothing(x):
	pass

# capture video from main camera
cap = cv2.VideoCapture(0)

# creating actuall window for tracking hsv
cv2.namedWindow("Tracking")

# creating trackbars on tracking window for hsv
cv2.createTrackbar("Lower Hue", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Lower Saturation", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Lower Value", "Tracking", 255, 255, nothing)

cv2.createTrackbar("Upper Hue", "Tracking", 255, 255, nothing)
cv2.createTrackbar("Upper Saturation", "Tracking", 255, 255, nothing)
cv2.createTrackbar("Upper Value", "Tracking", 255, 255, nothing)

# main loop
while True:
	# reading camera capture
	_, frame = cap.read()

	# converting image to hsv(hue, saturation, value)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# tracking trackbar value
	lower_hue = cv2.getTrackbarPos("Lower Hue", "Tracking")
	lower_saturation = cv2.getTrackbarPos("Lower Saturation", "Tracking")
	lower_value = cv2.getTrackbarPos("Lower Value", "Tracking")

	upper_hue = cv2.getTrackbarPos("Lower Hue", "Tracking")
	upper_saturation = cv2.getTrackbarPos("Lower Saturation", "Tracking")
	upper_value = cv2.getTrackbarPos("Lower Value", "Tracking")

	# lower blue threshold value
	lower_blue = numpy.array([lower_hue, lower_saturation, lower_value])

	# upper blue threshold value
	upper_blue = numpy.array([upper_hue, upper_saturation, upper_value])

	# mask for setting those two blue threshold values
	mask = cv2.inRange(hsv, lower_blue, upper_blue)

	# comparing images with bitwise operation
	result = cv2.bitwise_and(frame, frame, mask=mask)

	# displaying images
	cv2.imshow("frame", frame)
	cv2.imshow("mask", mask)
	cv2.imshow("result", result)

	# event key handler
	key = cv2.waitKey(1)

	# if event key is pressed condition
	if key == ord("q"):
		break

# releasing the camera source
cap.release()

# destroying all windows
cv2.destroyAllWindows()