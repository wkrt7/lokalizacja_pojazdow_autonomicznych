import numpy as np


def centerOfMass(img=None,obj_num_total=None,obj_num=None):
    """
    
    :param img: 
    :param obj_num_total: 
    :param obj_num: 
    :return: vec = vector of ints of center of mass found objects
    where vec[0,0] is x-coordinate of first object vec[0,1] is y-coordinate
    """
    M00 = np.empty(shape=[obj_num_total])
    M10 = np.empty(shape=[obj_num_total])
    M01 = np.empty(shape=[obj_num_total])

    for key, value in obj_num.iteritems():
        if key != 0:
            M00[key-1] = value

    for i in range(len(M00)):
        tmp = np.where(img == i+1)
        M01[i] = sum(tmp[0])
        M10[i] = sum(tmp[1])
    # print M00
    # print M10
    # print M01
    x = M10/M00
    y = M01/M00

    vec = np.column_stack((x.astype(int),y.astype(int)))
    ret_code = vec
    return ret_code

if __name__ == "__main__":
    centerOfMass()
