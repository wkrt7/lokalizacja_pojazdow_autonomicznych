import cv2, os
from Label import label
import numpy as np
from CenterOfMass import centerOfMass
from DetectEdges import detect_edges
import time

def recognizeCar():
    path = os.path.join('..', 'Data', 'mapa_autka.jpg')
    img = cv2.imread(path)
    # img = cv2.resize(img, (600, 600))
    # Converting to binary image
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    ret, thresh = cv2.threshold(img, 190, 255, cv2.THRESH_BINARY)

    # Labelling
    img_labeled, obj_num_total = label(thresh)
    print('liczba znalezionych obietkow %i' % obj_num_total)

    # Counting how many of each object there is in img
    unique, counts = np.unique(img_labeled, return_counts=True)
    obj_num = dict(zip(unique, counts))
    print obj_num

    # Counting center of mass labelled objects
    mass_vec = centerOfMass(img_labeled, obj_num_total=obj_num_total, obj_num=obj_num)
    print mass_vec

    d1, d2, d3, d4 = detect_edges(mass_vec)
    print d1

if __name__ == "__main__":
    start_time = time.time()
    recognizeCar()
    print 'Execution time: %f [s]' %(start_time - time.time())