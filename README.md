# Corner Detection and Downsampling

## Overview

This project includes Python scripts for corner detection (`corner.py`), downsampling (`downsample.py`), and edge detection (`edge.py`). The main functionalities are implemented in the `utils.py` file.

## Harris Corner Detection

### File: `corner.py`

- Functionality: Computes Harris corner response map using the formula R = Det(M) - k(Trace(M)^2).
- Inputs:
  - `img`: Grayscale image of shape (H, W).
  - `window_size`: Size of the window function.
  - `k`: Sensitivity parameter.
- Outputs:
  - `response`: Harris response image of shape (H, W).
- How to Use:
  ```python
  from corner import harris_corners, main
  response = harris_corners(img, window_size=3, k=0.04)
  ```
### Example Visualization
1. Harris response:
  ```
  python
  plt.imshow(corner_response, cmap='gray')
  plt.title('Image 1: Harris response')
  plt.show()
  ```
2. Harris map with threshold on response:
  ```
  python
  plt.imshow(threshold_response, cmap='gray')
  plt.title('Image 2: Harris map with threshold on response')
  plt.show()
  ```
3. Non-max suppression:
  ```
  python
  plt.imshow(img, cmap='gray')
  plt.plot(suppression[:, 1], suppression[:, 0], 'rx', markersize=20)
  plt.axis('off')
  plt.title('Image 3: Non-max suppression')
  plt.show()
  ```

## Downsampling
### File: downsample.py
- Functionality: Demonstrates naive subsampling and subsampling without aliasing.
- Inputs:
  - im: RGB image.
  - N_levels: Number of levels for downsampling.
- How to Use:
  ```
  python
  from downsample import main
  main()
  ```
### Example Visualization
1. Naive subsampling:
  ```
  python
  plt.imshow(im_subsample)
  ```
Subsampling without aliasing:
  ```
  python
  plt.imshow(downsampled)
  ```

## Edge Detection
### File: edge.py
- Functionality: Smooths an image with a Gaussian kernel, computes x and y derivatives, and visualizes the gradient magnitude.
- Inputs:
  - img: Grayscale image.
- How to Use:
  ```
  python
  from edge import main
  main()
  ```
### Example Visualization
1. Gradient on x:
  ```
  python
  plt.imshow(part_x, cmap='gray')
  plt.title('Image 1: Gradient on x')
  ```
2. Gradient on y:
  ```
  python
  plt.imshow(part_y, cmap='gray')
  plt.title('Image 2: Gradient on y')
  ```
3. Gradient magnitude:
  ```
  python
  plt.imshow(grad_mag, cmap='gray')
  plt.title('Image 3: Gradient magnitude')
  plt.show()
  ```

## Utils
### File: utils.py
- Functionality: Contains utility functions for creating a Gaussian kernel, zero-padding an image, and performing 2D filtering.
- Functions:
  - gaussian_kernel
  - zero_pad
  - filter2d
  - partial_x
  - partial_y
### How to Use
1. Install Dependencies: Ensure you have the required libraries installed:
```
bash
pip install numpy matplotlib scikit-image
```
2. Clone the Repository: Clone the repository to your local machine.
```
bash
git clone [repository_url]
cd [repository_directory]
```
3. Run the Scripts: Execute the scripts (corner.py, downsample.py, edge.py) to observe the results.
```
bash
python corner.py
python downsample.py
python edge.py
```

## Author
Ismael Rekik
