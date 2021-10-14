import cv2
import os
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.image as mpimg

"""
directory_path = "/project_kntt"

list_path = []

#img = cv2.imread()
for i in os.listdir("/project_kntt"):
	if i.endswith(".jpg"):
		list_path.append(os.path.join(directory_path,i))


print(list_path)

img = cv2.imread(list_path[0])
#img = cv2.blur(img, (5,5))
blur = cv2.bilateralFilter(img,9,75,75)
cv2.imshow("img1",blur)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_resize = cv2.resize(img, dsize = (200,130))


_, threshold = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)
#adapt = adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
"""

def fourNeighborPoint(array,x,y):
	if x == array.shape[0] - 1 or y == array.shape[1] - 1:
		return array[x][y]
	if array[x+1][y] == 0:
		return 128
	if array[x-1][y] == 0:
		return 128
	if array[x][y+1] == 0:
		return 128
	if array[x][y-1] == 0:
		return 128
	return array[x][y]

def findArea(array):
	for i in range(array.shape[0]):
		for j in range(array.shape[1]):
			if array[i][j] == 255:
				array[i][j] = fourNeighborPoint(array,i,j)

img = cv2.imread("cmt1.jpg")

img = cv2.resize(img, dsize = (800, 650))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
adapt = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 11)
#cv2.imshow("img",adapt)
#cv2.waitKey(0)

adapt1 = np.array(adapt)

cols, rows = adapt1.shape
print(rows,cols)


for i in range(cols):
	for j in range(rows):
		if adapt1[i][j] == 255:
			adapt1[i][j] = 0
		else:
			adapt1[i][j] = 255

roi = adapt1[200:240, 370:400]
findArea(adapt1)

"""
for i in range(roi.shape[0]):
	for j in range(roi.shape[1]):
		print(roi[i][j], end = "  ")
	print("\n")
"""

img_plt = plt.imshow(adapt1)
plt.show()

