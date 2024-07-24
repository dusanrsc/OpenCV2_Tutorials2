# importing module
import cv2

# handling video ("videoPath" or camera index 0, 1, 2) 
cap = cv2.VideoCapture(0)

# fourcc
fourcc = cv2.VideoWriter_fourcc(*"XVID")

# writing/saving video (videoPath, fourcc, fps, videoSize)
out = cv2.VideoWriter("assets/output.avi", fourcc, 20.0, (640, 480))

# getting width and height parameters
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# while cap.qisOpened() = true
# if cap.isOpened() = false try cap.open()
while (cap.isOpened()):
	# ret=true/false, frame=actual image
	ret, frame = cap.read()

	# if return is true
	if ret:
		# printing width and height
		print(width, height)

		# save/write instance of frame in output
		out.write(frame)

		# convert colored image into grayscale
		grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# displaying main windows with image
		cv2.imshow("Tutorial4", grayscale)

		# break loop by event/key press
		if cv2.waitKey(1) & 0xFF == ord("q"):
			break

	# break loop if return is false
	else:
		break

# release the camera source
cap.release()

# release the output source
out.release()

# destroy all windows
cv2.destroyAllWindows()