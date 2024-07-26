# importing moduels
import cv2
import numpy

# variables section
# loading image ("imagePath", colorChannels= -1, 0, 1)
img = cv2.imread("assets/soccer_practice.jpg", 0)

# creating your own image with nupmy matrix
# numpy.zeros is black ([imageWidth, numpyHeight], dataType)
img = numpy.zeros([1024, 1024, 3], numpy.uint8)

# this wasnt on the tutorial but image is to large
# processing image (resizing)
resized_img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# drawing objects on image section
# draw line on the image (imageVariable, (startingPointX, startingPointY), (endingPointX, endingPointY), (blueColor, greenColor, redColor), tickness)
drawing_line_on_resized_img = cv2.line(resized_img, (20, 20), (20, 400), (255, 0, 0), 5)

# drawing arrowed line on the image (imageVariable, (startingPointX, startingPointY), (endingPointX, endingPointY), (blueColor, greenColor, redColor), tickness)
drawing_arrowed_line_on_resized_img = cv2.arrowedLine(resized_img, (50, 40), (400, 40), (255, 255, 255), 3)

# drawing rectangle on the image (imageVariable, (startingPointX, startingPointY), (endingPointX, endingPointY), (blueColor, greenColor, redColor), tickness) tickness -1 is filled
drawing_rectangle_on_resized_img = cv2.rectangle(resized_img, (80, 80), (250, 150), (0, 255, 50), -1)

# drawing circle on the image (startingPointX, startingPointY), (circleRadius), (blueColor, greenColor, redColor), tickness)
drawing_circle_on_resized_img = cv2.circle(resized_img, (300, 110), (30), (255, 255, 0), 5)

# text must have font instance and drawing text
# font instance
font = cv2.FONT_HERSHEY_SIMPLEX
# drawing text (imageVariable, "textString", (startingPointX, startingPointY), fontInstance, fontSize, (blueColor, greenColor, redColor), tickness, drawingMethod)
drawing_text_on_resized_img = cv2.putText(resized_img, "Tutorial5", (100, 125), font, 1, (0, 255, 255), 3, cv2.LINE_AA)

# displaying image window ("windowTitle, imageVariable")
display_img = cv2.imshow("Tutorial5", drawing_arrowed_line_on_resized_img)

# setting waitkey as 0/infinity
# also press any key to destroy all windows
cv2.waitKey(0)

# destroying all windows
cv2.destroyAllWindows()