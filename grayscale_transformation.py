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


def logarithmic_transformation(img_input):
    x, y = np.where((img_input >= 0) & (img_input <= 255))
    c = 255 / np.log1p(np.max(img_input))
    img_input[x, y] = c * np.log1p(img_input[x, y])


def gamma_transformation(img_input, poynton = 1.0):
    x, y = np.where((img_input >= 0) & (img_input <= 255))
    c = 255 / np.power(np.max(img_input), poynton)
    img_input[x, y] = c * np.power(img_input[x, y], poynton)
    # img_input[x, y] = np.power((img_input[x, y] / 255), poynton) * 255


# img = cv.imread("resource/srcImg.png", cv.IMREAD_GRAYSCALE)
img = cv.imread("resource/Fig0305(a)(DFT_no_log).tif", cv.IMREAD_GRAYSCALE)
# img = cv.imread("resource/Fig0309(a)(washed_out_aerial_image).tif", cv.IMREAD_GRAYSCALE)
# img = cv.imread("resource/Fig0308(a)(fractured_spine).tif", cv.IMREAD_GRAYSCALE)
start = time.perf_counter()
# grayscale_inversion(img)
logarithmic_transformation(img)
# gamma_transformation(img, 5.0)
end = time.perf_counter()
print(end - start)
# cv.normalize(img, img, 0, 255, cv.NORM_MINMAX)
# cv.convertScaleAbs(img, img)
cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()
