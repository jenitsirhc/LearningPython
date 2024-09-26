import numpy as np
from multiprocessing import Pool, TimeoutError
import cv2
import matplotlib.pylab as plt
import os
import multiprocessing 
import time


print()
print("Number of processors available in this device: ", multiprocessing.cpu_count())

height = 512
width = 512

image_file = {"blurredImage.jpg": np.zeros((height, width, 3), np.uint8),
              "cat.jpg": np.ones((height, width, 3), np.uint8)}

list_images = list(image_file)

def read_function (): 
    print(f"Processing..")
    img_in = list_images[img_in]
    img_resized = cv2.resize(image_file, None, fx=0.25, fy=0.25)
    kernel_sharpening = np.array([[-1,-1,-1], 
                                    [-1,9,-1], 
                                    [-1,-1,-1]])
    sharpened = cv2.filter2D(img_resized, -1, kernel_sharpening)
    img_rgb = cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB)
    cv2.imwrite(f"parallelImages(jpg)/0.jpg",img_rgb)
    print("Processing successful")
    return True

def create_pool():
    coordinates = []
    with Pool(processes=4) as pool:
        files_to_precess = [pool.apply_async(read_function, args=("images(jpg)" + daytime_images[number], 31, 90, 170))
                            for number in range(number_of_day_images)]
        try:
            coordinates = [res.get() for res in files_to_precess]  # processes get your data in here
        except TimeoutError:
            print("We lacked patience and got a multiprocessing.TimeoutError")
    return coordinates

if __name__ == '__main__':
    start = time.perf_counter()

    daytime_images = os.listdir("D/TR/Daytime/")
    number_of_day_images = len(daytime_images)
    print(number_of_day_images)
    day_value = 27
    coordinates = create_pool()
    [print(res) for res in coordinates]

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s))")

