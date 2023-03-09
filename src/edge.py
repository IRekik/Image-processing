import numpy as np
import matplotlib.pylab as plt
from skimage import io
from utils import gaussian_kernel, filter2d, partial_x, partial_y

def main():
    # Load image
    img = io.imread('iguana.png', as_gray=True)

    ### YOUR CODE HERE

    # Smooth image with Gaussian kernel
    kernel = gaussian_kernel(l=5, sig=1.)
    smoothed = filter2d(img, kernel)

    # Compute x and y derivate on smoothed image
    part_x = partial_x(smoothed)
    part_y = partial_y(smoothed)

    # Compute gradient magnitude
    grad_mag = np.sqrt(np.square(part_x) + np.square(part_y))

    # Visualize results
    plt.subplot(2, 2, 1)
    plt.imshow(part_x, cmap = 'gray')
    plt.title('Image 1: Gradient on x')

    plt.subplot(2, 2, 2)
    plt.imshow(part_y, cmap = 'gray')
    plt.title('Image 2: Gradient on y')

    plt.subplot(2, 2, 3)
    plt.imshow(grad_mag, cmap = 'gray')
    plt.title('Image 3: Gradient magnitude')

    plt.show()

    ### END YOUR CODE
    
if __name__ == "__main__":
    main()

