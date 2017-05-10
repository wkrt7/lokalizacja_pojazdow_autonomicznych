import cv2
import time
import numpy as np


def detect_edges(obj=None,img=None):
    """
    
    :param obj: vector of mass center
    :param img: only for purpose of knowing size of image to calculate distance from objects to corners of image
    :return: coordinates of corners of box
    """
    x = obj[:, 0]
    y = obj[:, 1]
    y_max = len(img)  # Need info about size of pic to calculate distance from corner
    x_max = len(img[0])  # Need info about size of pic to calculate distance from corner

    # Calculating euclidean distance between points: may be faster
    d1_arg = np.argmin(np.square(obj[:, 0] - 0) + np.square(obj[:, 1] - 0))
    d2_arg = np.argmin(np.square(obj[:, 0] - x_max) + np.square(obj[:, 1] - 0))
    d3_arg = np.argmin(np.square(obj[:, 0] - x_max) + np.square(obj[:, 1] - y_max))
    d4_arg = np.argmin(np.square(obj[:, 0] - 0) + np.square(obj[:, 1] - y_max))

    d1 = obj[d1_arg, :]
    d2 = obj[d2_arg, :]
    d3 = obj[d3_arg, :]
    d4 = obj[d4_arg, :]

    ret_code = d1, d2, d3, d4
    return ret_code

if __name__ == '__main__':
    start_time = time.time()
    detect_edges()
    print 'Execution time: %f [s]' % (start_time - time.time())
