import cv2 as cv
import numpy as np
import time


def grayscale_inversion(img_input):
    # img_output = img.copy()
    # for i, color in np.ndenumerate(img_input):
    #     img_input[i] = 255 - color
    # x, y = img_input.nonzero()
    x, y = np.where((img_input >= 0) & (img_input <= 255))
    img_input[x, y] = 255 - img_input[x, y]
    # img_output = np.where(img_input >= 0, 255 - img_input, 0)
    # print(img_output)
    # return img_output


img = cv.imread("resource/srcImg.png", cv.IMREAD_GRAYSCALE)
start = time.perf_counter()
grayscale_inversion(img)
end = time.perf_counter()
print(end - start)
cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()
