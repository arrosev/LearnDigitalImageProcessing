import cv2 as cv
import numpy as np


def grayscale_inversion(img_input):
    # img_output = img.copy()
    for i, color in np.ndenumerate(img_input):
        img_input[i] = 255 - color


img = cv.imread("resource/srcImg.png", cv.IMREAD_GRAYSCALE)
grayscale_inversion(img)
cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()
