# Display a colored image with matplotlib
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('messi.jpg', cv.IMREAD_COLOR)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)  # convert from BGR to RGB
plt.imshow(img)
plt.xticks([]), plt.yticks([])  # to hide the tick values on X & Y axis
plt.show()
