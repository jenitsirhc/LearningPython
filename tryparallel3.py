import numpy as np
from glob import glob
import cv2
import matplotlib.pylab as plt
import time
import multiprocessing 
import time


print()
print("Number of processors available in this device: ", multiprocessing.cpu_count())

image_file = glob("images(jpg)/*.jpg")

start = time.perf_counter()

def read_function():
    
        print(f"Processing..{ctr}")
        img = plt.imread(image_file[ctr])
        img_resized = cv2.resize(img, None, fx=0.25, fy=0.25)
        kernel_sharpening = np.array([[-1,-1,-1], 
                                    [-1,9,-1], 
                                    [-1,-1,-1]])
        sharpened = cv2.filter2D(img_resized, -1, kernel_sharpening)
        img_rgb = cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB)
        cv2.imwrite(f"parallelImages(jpg)/{ctr}.jpg",img_rgb)
        print("Processing successful")



processes = []
if __name__ == '__main__':
    for _ in range(10):
        s = multiprocessing.Process(target=read_function)
        s.start()
        processes.append(s)
        
        for process in processes:
            process.join()
    
   
finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s))")

