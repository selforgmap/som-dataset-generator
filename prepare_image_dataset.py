#!/usr/bin/env python3

import sys, os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Validate inputs
if (len(sys.argv) == 1):
	print("usage: prepare_image_dataset.py directory")
	exit(0)

# Process image
def processImage(img):
	imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	imcolor = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	
	ret, thresh = cv2.threshold(imgray, 127, 255, 0)
	im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	return imgray


dataset = np.array([[]])

# For each image file
for filename in os.listdir(sys.argv[1]):
	if (filename[0] == '.'): continue
	path = sys.argv[1] + '/' + filename

	# Open image
	print(path)
	img = cv2.imread(path)
	imgData = processImage(img).ravel().astype(int)

	# Add to dataset
	if (dataset.size == 0):
		dataset = np.array(imgData)
	else:
		dataset = np.vstack([dataset, imgData])


# Save dataset
print("Saving dataset\n", dataset)
np.savetxt("dataset.csv", dataset, fmt='%i', delimiter=",")

