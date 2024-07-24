# importing module
import cv2

# loading image ("imagePath", colorChannels= -1, 0, 1)
img = cv2.imread("assets/soccer_practice.jpg", 0)

# this wasnt on the tutorial but image is to large
# processing image (resizing)
resized_img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# printing matric/multidimensional list of arrys of image
print(resized_img)

# displaying image window ("windowTitle, imageVariable")
cv2.imshow("Image", resized_img)

# displaying image window (0=infinite, or in milisecconds)
key = cv2.waitKey(0) & 0xFF		# 0xFF is mask that returns 8 bit integer value

# if event key is 27/esc
if key == 27:
	# destroying all windows
	cv2.destroyAllWindows()		# or single window destroy cv2.destroyWindow

# elif event key is s
elif key == ord("s"):
	# writing/saving image ("imagePath", imageVariable)
	cv2.imwrite("assets/soccer_practice_resized_grayscale.jpg", resized_img)
	
	# destroying all windows
	cv2.destroyAllWindows()