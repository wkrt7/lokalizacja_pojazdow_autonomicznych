import numpy as np


def centerOfMass(img=None,obj_num_total=None,obj_num=None):

    M00 = np.empty(shape=[obj_num_total])
    M10 = np.empty(shape=[obj_num_total])
    M01 = np.empty(shape=[obj_num_total])

    for key, value in obj_num.iteritems():
        if key != 0 :
            M00[key-1] = value

    for i in range(len(M00)):
        tmp = np.where(img == i+1)
        M10[i] = sum(tmp[0])
        M01[i] = sum(tmp[1])
    # print M00
    # print M10
    # print M01
    x = M10/M00
    y = M01/M00
    return x, y

if __name__ == "__main__":
    centerOfMass()
