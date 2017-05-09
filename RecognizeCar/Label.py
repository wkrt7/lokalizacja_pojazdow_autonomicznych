from skimage import measure


def label(img=None):
    """ 
    IN:
    img - binary image
    OUT:
    returns labelled image, number of detected objects
    """
    labelled_img = measure.label(img)
    # labelled_img = measure.label(img, background=0)
    obj_num = labelled_img.max()

    return labelled_img, obj_num


if __name__ == "__main__":
    label()
