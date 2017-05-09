import cv2, os
from Label import label
import numpy as np
from CenterOfMass import centerOfMass
import time

def recognizeCar():
    path = os.path.join('..', 'Data', 'test3.png')
    img = cv2.imread(path)
    # Converting to binary image
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # Labelling
    img_labeled, obj_num_total = label(thresh)
    print('liczba znalezionych obietkow %i' % obj_num_total)
    # Counting how many of each object there is in img
    unique, counts = np.unique(img_labeled, return_counts=True)
    obj_num = dict(zip(unique, counts))
    print obj_num
    x, y = centerOfMass(img_labeled,obj_num_total=obj_num_total,obj_num=obj_num)

if __name__ == "__main__":
    start_time = time.time()
    recognizeCar()
    print 'Execution time: %f [s]' %(start_time - time.time())