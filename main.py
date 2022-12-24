
import cv2 as cv
print(cv.__version__)

img = cv.imread("resource/srcImg.png")
cv.imshow("2", img)
cv.waitKey(0)
cv.destroyAllWindows()
