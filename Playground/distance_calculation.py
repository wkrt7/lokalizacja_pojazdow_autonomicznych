import numpy as np


def distance_calculation(p1=[0,0], p2=[1,1], box_size = [1, 1]):
    """
    Inputs: p = [a.b]
    """
    a_dist = box_size[0]*np.abs(p1[0]-p2[0])
    b_dist = box_size[1]*np.abs(p1[1]-p2[1])

    ret_code = np.sqrt(a_dist*a_dist + b_dist*b_dist)

    return ret_code

if __name__ == "__main__":
    ret = distance_calculation([0.0, 1.0],[1.0, 0.0], [3,4])
    print ret
