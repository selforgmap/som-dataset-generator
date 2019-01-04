#!/usr/bin/env python3

import sys, os
import cv2
import numpy as np
import matplotlib.pyplot as plt


# Validate inputs
if (len(sys.argv) < 3):
	print("Usage: image_to_array.py <image> <process>")
	exit(0)

# Load params
path = sys.argv[1]
process = sys.argv[2]
preview = False
if (len(sys.argv) == 4 and sys.argv[3] == "-preview"): preview = True

# Process image
def processImage(img, p):
	if   (p == "gray"):      res = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)     # Gray
	elif (p == "laplacian"): res = cv2.Laplacian(img, cv2.CV_64F)            # Laplacian
	elif (p == "sobelx"):    res = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5) # Sobel X
	elif (p == "sobely"):    res = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5) # Sobel Y
	elif (p == "canny"):     res = cv2.Canny(img, 100, 200)                  # Canny Edges
	elif (p == "threshold"): x, res = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

	return res

# View image
def viewImage(img):
	cv2.imshow('image',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

# Load image
img = cv2.imread(path)
outImage = processImage(img, process)

if (preview):
	viewImage(outImage)
else:
	# Save dataset
	dataset = outImage.ravel().astype(int)
	datasetStr = ",".join(dataset.astype(str))
	print(datasetStr)
