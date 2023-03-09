import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from utils import gaussian_kernel, filter2d

def main():
    
    # load the image
    im = imread('paint.jpg').astype('float')
    im = im / 255

    im = rgb2gray(im)

    # number of levels for downsampling
    N_levels = 5

    # make a copy of the original image
    im_subsample = im.copy()

    # naive subsampling, visualize the results on the 1st row
    for i in range(N_levels):
        #subsample image 
        im_subsample = im_subsample[::2, ::2]
        plt.subplot(2, N_levels, i+1)
        plt.imshow(im_subsample)
        plt.axis('off')

    # subsampling without aliasing, visualize results on 2nd row

    #### YOUR CODE HERE
    for i in range(N_levels):
        # create gaussian kernel
        kernel = gaussian_kernel(l = 5, sig = 1)

        # gaussian filter
        filtered = filter2d(im, kernel)

        #downsample image
        downsampled = filtered[::2, ::2]

        im = downsampled

        plt.subplot(3, N_levels, N_levels+1+i)
        plt.imshow(downsampled)
    plt.show()
    #### END YOUR CODE
    
if __name__ == "__main__":
    main()
