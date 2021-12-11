import cv2
import numpy as np


#1.

img_gray = cv2.imread("images/kamera3.jpg", cv2.IMREAD_GRAYSCALE)
print("Dimenzije: ", img_gray.shape)
cv2.imshow("Gray", img_gray)
cv2.imwrite("images/kamera2_gray.jpg", img_gray)


#2.
img = cv2.imread("images/kamera3.jpg", cv2.IMREAD_COLOR)
res = cv2.resize(img, (1000,650))
cv2.imshow("Resized", res)
print("Nove dim: ", res.shape)


#3.

img_y = img
img_y[265:280, 135:165, :] = [0,255,255]
cv2.imshow("img", img_y)

#4.
img_yhsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_yhsv[265:280, 135:165, :] = [30, 255, 255]
cv2.imshow("HSV", cv2.cvtColor(img_yhsv, cv2.COLOR_HSV2BGR))

#5.

_, bin = cv2.threshold(img_gray, img.mean(), 255, cv2.THRESH_BINARY)
cv2.imshow("BIN", bin)

#6.
sem = cv2.imread("images/crveni_semafor.jpg", cv2.IMREAD_COLOR)
sem = cv2.cvtColor(sem, cv2.COLOR_BGR2HSV)
sem = cv2.resize(sem, None, fx=3, fy=3)

lower = np.array([170,50,50])
upper = np.array([180,255,255])

maska = cv2.inRange(sem, lower, upper)

filtered = cv2.bitwise_and(sem, sem, mask=maska)
filtered_bgr = cv2.cvtColor(filtered, cv2.COLOR_HSV2BGR)
cv2.imshow("Pixel", filtered_bgr)


#7.
im1 = cv2.imread("images/kamera4.png", cv2.IMREAD_GRAYSCALE)
blured = cv2.GaussianBlur(im1, (5,5), 0)

sobel_x = cv2.Sobel(blured, cv2.CV_64F, 1, 0 , ksize=5)
sobel_y = cv2.Sobel(blured, cv2.CV_64F, 0, 1, ksize=5)

sobel_x_abs = cv2.convertScaleAbs(sobel_x)
sobel_y_abs = cv2.convertScaleAbs(sobel_y)
cv2.imshow("Sobel x", sobel_x_abs)
cv2.imshow("Sobel y", sobel_y_abs)

#8.
canny = cv2.Canny(im1, 100, 200)
cv2.imshow("Canny", canny)



cv2.waitKey(0)
cv2.destroyAllWindows()
