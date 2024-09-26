#IMAGE RESIZING AND IMAGE SHARPENING ; IMAGE PROCESSING
import pandas as pd
import numpy as np
from glob import glob
import cv2
import matplotlib.pylab as plt
import time

#Select all jpg images
image_file = glob("images(jpg)/*.jpg")

#Timer STARTS here
start = time.perf_counter()

img_mpl = plt.imread(image_file[1])
img_cv2 = cv2.imread(image_file[1])
img_mpl.shape, img_cv2.shape
img = plt.imread(image_file[1])

kernel_sharpening = np.array([[-1,-1,-1], 
                              [-1,9,-1], 
                              [-1,-1,-1]])

sharpened = cv2.filter2D(img, -1, kernel_sharpening)
img_resized = cv2.resize(img, None, fx=0.25, fy=0.25)
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(sharpened)
plt.show()

#Timer ENDS here
finish = time.perf_counter()