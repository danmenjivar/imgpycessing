# Display an image with matplotlib
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('messi.jpg', cv.IMREAD_GRAYSCALE)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hide the tick values on X & Y axis
plt.show()
