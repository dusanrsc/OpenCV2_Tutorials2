# importing module
import cv2

# video captuing variable from main camera
cap = cv2.VideoCapture(0)

# printing frame width and height
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# main program loop
# while capturing is opened returning true
while (cap.isOpened()):

	# returning frame success and actual frame
	ret, frame = cap.read()

	# if returned is true condition
	if ret == True:
		# convert frame fo grayscale
		grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		
		# displaying the frame of video capture
		cv2.imshow("Tutorial6", grayscale)

		# if event key is q break the loop
		if cv2.waitKey(1) & 0xFF == ord("q"):
			break

	# break the loop when returns false
	else:
		break

# liberating main camera
cap.release()

# destroying all windows
cv2.destroyAllWindows()