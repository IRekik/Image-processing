import numpy as np
import matplotlib.pylab as plt
from skimage import io
from utils import gaussian_kernel, filter2d, partial_x, partial_y

def main():
    # Load image
    img = io.imread('iguana.png', as_gray=True)

    ### YOUR CODE HERE

    # Smooth image with Gaussian kernel
    kernel = gaussian_kernel()
    smoothed = filter2d(img, kernel)

    # Compute x and y derivate on smoothed image
    part_x = partial_x(smoothed)
    part_y = partial_y(smoothed)

    # Compute gradient magnitude
    grad_mag = np.sqrt(np.square(part_x) + np.square(part_y))

    # Visualize results
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Before')
    plt.subplot(1, 2, 2)
    plt.imshow(grad_mag, cmap='gray')
    plt.title('After')
    plt.show()

    ### END YOUR CODE
    
if __name__ == "__main__":
    main()

