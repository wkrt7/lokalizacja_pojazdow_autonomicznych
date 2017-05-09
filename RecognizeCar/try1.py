from skimage import measure
try:
    from skimage import filters
except ImportError:
    from skimage import filter as filters
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
n = 12
l = 256
np.random.seed(1)
im = np.zeros((l, l))
points = l * np.random.random((2, n ** 2))
im[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
im = filters.gaussian_filter(im, sigma= l / (4. * n))
blobs = im > 0.7 * im.mean()
path = os.path.join('..', 'Data', 'test1.png')
img = cv2.imread(path)
# Converting to binary image
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

all_labels = measure.label(thresh)
blobs_labels = measure.label(thresh, background=0)
print all_labels.max()
plt.figure(figsize=(9, 3.5))
plt.subplot(131)
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.subplot(132)
plt.imshow(all_labels, cmap='spectral')
plt.axis('off')
plt.subplot(133)
plt.imshow(blobs_labels, cmap='spectral')
plt.axis('off')

plt.tight_layout()
plt.show()