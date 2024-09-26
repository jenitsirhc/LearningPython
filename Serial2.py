#IMAGE RESIZING AND IMAGE SHARPENING ; IMAGE PROCESSING
import numpy as np
from glob import glob
import cv2
import matplotlib.pylab as plt
import time

#Select all jpg images
image_file = glob("images(jpg)/*.jpg")

print()
print("Serial :")
print()

#Timer STARTS here
start = time.perf_counter()

ctr = 0
while ctr < len(image_file):

#FIRST IMAGE
    img = plt.imread(image_file[ctr])

    #Sharpening the image
    kernel_sharpening = np.array([[-1,-1,-1], 
                                [-1,9,-1], 
                                [-1,-1,-1]])

    sharpened = cv2.filter2D(img, -1, kernel_sharpening)
    #Resizing the image
    img_resized = cv2.resize(sharpened, None, fx=0.25, fy=0.25)
    #Coverting BGR to RGB
    img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
    #Saving the image
    cv2.imwrite(f"serialImages(jpg)/{ctr}.jpg",img_rgb)
    ctr+=1
    print("Processed Image: ", ctr)


#Timer ENDS here
finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s))")
