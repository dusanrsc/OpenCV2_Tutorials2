# importing module
import cv2

# function for clicking
def click_event(event, x, y, flags, parameters):
	# on left mouse button down
	if event == cv2.EVENT_LBUTTONDOWN:
		# creating circle
		cv2.circle(resized_img, (x, y), 3, (0, 0, 255), -1)
		
		# adding x and y coords in empty point list
		points.append((x, y))
		
		# checking if length of list is greather than 2
		if len(points) >= 2:
			# draw the connecting line beetween two points
			cv2.line(resized_img, points[-1], points[-2], (255, 0, 0), 2)

		# displaying img
		cv2.imshow("Tutorial9A", resized_img)

# loading img
img = cv2.imread("assets/soccer_practice.jpg")

# this wasnt on the tutorial but image is to large
# processing image (resizing)
resized_img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# displaying img
cv2.imshow("Tutorial9A", resized_img)

# creating empty list variable
points = []

# setting mouse callback when is clicked
cv2.setMouseCallback("Tutorial9A", click_event)

# not allowing window to close
cv2.waitKey(0)

# destroying all windows
cv2.destroyAllWindows()
