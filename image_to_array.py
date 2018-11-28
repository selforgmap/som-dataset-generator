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
	# res = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	res = cv2.Canny(img,100,200)
	return res


# Load image
path = sys.argv[1]
img = cv2.imread(path)
dataset = processImage(img).ravel().astype(int)

# Dataset to string
datasetStr = ",".join(dataset.astype(str))
print(datasetStr)
