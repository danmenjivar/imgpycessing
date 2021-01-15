# Tutorial on How to read an image and save it back using OpenCV
import numpy as np
import cv2 as cv
# load an image in grayscale
img = cv.imread("messi.jpg", cv.IMREAD_GRAYSCALE)
cv.imshow("image", img)  # show the image
key = cv.waitKey(0)
if key == 27:  # wait for ESC (27 is ASCII) key to exit
    cv.destroyAllWindows()
elif key == ord('s'):  # wait for 's' to save and exit (ord returns ascii value)
    cv.imwrite("messigray.jpg", img)
    cv.destroyAllWindows()
