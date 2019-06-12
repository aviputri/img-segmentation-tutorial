from skimage.color import rgb2gray
import numpy as np
import cv2
import PyQt5
import matplotlib
matplotlib.get_backend()
matplotlib.use('qt5agg')
import matplotlib.pyplot as plt
#%matplotlib inline
from scipy import ndimage

image = plt.imread('index.png')
plt.imshow(image)
plt.show()

"""
It should be fairly simple for us to understand how the edges are detected in this image. 
Let’s convert it into grayscale and define the sobel filter (both horizontal and vertical) 
that will be convolved over this image:
"""

# converting to grayscale
gray = rgb2gray(image)

# defining the sobel filters
sobel_horizontal = np.array([np.array([1, 2, 1]), np.array([0, 0, 0]), np.array([-1, -2, -1])])
print(sobel_horizontal, 'is a kernel for detecting horizontal edges')
 
sobel_vertical = np.array([np.array([-1, 0, 1]), np.array([-2, 0, 2]), np.array([-1, 0, 1])])
print(sobel_vertical, 'is a kernel for detecting vertical edges')


"""
Now, convolve this filter over the image using the convolve function of the ndimage package from scipy.
"""

out_h = ndimage.convolve(gray, sobel_horizontal, mode='reflect')
out_v = ndimage.convolve(gray, sobel_vertical, mode='reflect')
# here mode determines how the input array is extended when the filter overlaps a border.


"""
Let’s plot these results:
"""
plt.imshow(out_h, cmap='gray')
plt.show()

plt.imshow(out_v, cmap='gray')
plt.show()

"""
Here, we are able to identify the horizontal as well as the vertical edges. 
There is one more type of filter that can detect both horizontal and vertical edges at the same time. 
This is called the laplace operator:

1 	1 	1
1 	-8 	1
1 	1 	1
"""

#Let’s define this filter in Python and convolve it on the same image:
kernel_laplace = np.array([np.array([1, 1, 1]), np.array([1, -8, 1]), np.array([1, 1, 1])])
print(kernel_laplace, 'is a laplacian kernel')

#Next, convolve the filter and print the output:
out_l = ndimage.convolve(gray, kernel_laplace, mode='reflect')
plt.imshow(out_l, cmap='gray')
plt.show()