import cv2
import time


def detect_edges(obj=None):

    d1 = 1
    d2 = 2
    d3 = 3
    d4 = 4
    ret_code = d1, d2, d3, d4
    return ret_code

if __name__ == '__main__':
    start_time = time.time()
    detect_edges()
    print 'Execution time: %f [s]' % (start_time - time.time())