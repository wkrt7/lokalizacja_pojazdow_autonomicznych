import cv2
import time
import numpy as np

def detect_edges(obj=None):
    x = obj[:, 0]
    y = obj[:, 1]
    d1_arg = np.argmin(np.square(obj[:, 0]) + np.square(obj[:, 1]))
    d1 = obj[d1_arg, :]
    d2 = 2
    d3 = 3
    d4 = 4
    ret_code = d1, d2, d3, d4
    return ret_code

if __name__ == '__main__':
    start_time = time.time()
    detect_edges()
    print 'Execution time: %f [s]' % (start_time - time.time())
