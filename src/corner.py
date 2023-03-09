import numpy as np
from utils import filter2d, partial_x, partial_y
from skimage.feature import peak_local_max
from skimage.io import imread
import matplotlib.pyplot as plt

def harris_corners(img, window_size=3, k=0.04):
    """
    Compute Harris corner response map. Follow the math equation
    R=Det(M)-k(Trace(M)^2).
        
    Args:
        img: Grayscale image of shape (H, W)
        window_size: size of the window function
        k: sensitivity parameter

    Returns:
        response: Harris response image of shape (H, W)
    """

    response = None
    
    ### YOUR CODE HERE
    part_x = partial_x(img)
    part_y = partial_y(img)
    filter_x = filter2d(part_x**2, np.ones((window_size, window_size)))
    filter_y = filter2d(part_y**2, np.ones((window_size, window_size)))
    filter_x_y = filter2d(part_x * part_y, np.ones((window_size, window_size)))
    det = filter_x * filter_y - filter_x_y**2
    trace = filter_x + filter_y
    response = det - (k * (trace**2))
    ### END YOUR CODE

    return response

def main():
    img = imread('building.jpg', as_gray=True)

    ### YOUR CODE HERE
    
    # Compute Harris corner response
    corner_response = harris_corners(img, window_size = 3, k = 0.04)

    # Threshold on response
    threshold = 0.2 * np.max(corner_response)
    threshold_response = (corner_response > threshold) * corner_response

    # Perform non-max suppression by finding peak local maximum
    suppression = peak_local_max(threshold_response, min_distance = 10)

    # Visualize results
    plt.imshow(corner_response, cmap = 'gray')
    plt.title('Image 1: Harris response')
    plt.show()

    plt.imshow(threshold_response, cmap = 'gray')
    plt.title('Image 2: Harris map with threshold on response')
    plt.show()

    a, b = plt.subplots()
    b.imshow(img, cmap = 'gray')
    b.plot(suppression[:, 1], suppression[:, 0], 'rx', markersize = 20)
    b.axis('off')
    plt.title('Image 3: Non-max suppression')
    plt.show()
    ### END YOUR CODE
    
if __name__ == "__main__":
    main()
