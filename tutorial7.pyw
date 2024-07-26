# importing module
import cv2

# importing sub-modules
from time import strftime

# variable section
# video captuing variable from main camera
cap = cv2.VideoCapture(0)

# main program loop
# while capturing is opened returning true
while (cap.isOpened()):

	# returning frame success and actual frame
	ret, frame = cap.read()

	# if returned is true condition
	if ret == True:
		# convert frame fo grayscale
		grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# text must have font instance and drawing text
		# font instance
		font = cv2.FONT_HERSHEY_SIMPLEX

		# drawing date and time (imageVariable, "textString", (startingPointX, startingPointY), fontInstance, fontSize, (blueColor, greenColor, redColor), tickness, drawingMethod)
		drawing_date_and_time_on_grayscale_img = cv2.putText(grayscale, f"{strftime("%Y-%m-%d %H:%M:%S")}", (10, 20), font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

		# drawing frame width and height (imageVariable, "textString", (startingPointX, startingPointY), fontInstance, fontSize, (blueColor, greenColor, redColor), tickness, drawingMethod)
		drawing_frame_width_and_height_on_grayscale_img = cv2.putText(grayscale, f"w:{int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))}, h:{int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}", (10, 40), font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
		
		# displaying grayscale frame of the video capture
		cv2.imshow("Tutorial7", grayscale)

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