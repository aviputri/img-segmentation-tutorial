import PyQt5
import matplotlib
matplotlib.get_backend()
matplotlib.use('qt5agg')
import matplotlib.pyplot as plt
import numpy as np
from skimage import io
import skimage.data as data
import skimage.segmentation as seg
import skimage.filters as filters
import skimage.draw as draw
import skimage.color as color

def image_show(image, nrows=1, ncols=1, cmap='gray'):
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(14, 14))
    ax.imshow(image, cmap='gray')
    ax.axis('off')
    plt.show()
    return fig, ax

image = io.imread('girl.jpg') 
plt.imshow(image);
plt.show()

image_felzenszwalb = seg.felzenszwalb(image) 
image_show(image_felzenszwalb);

np.unique(image_felzenszwalb).size

image_felzenszwalb_colored = color.label2rgb(image_felzenszwalb, image, kind='avg')

image_show(image_felzenszwalb_colored)