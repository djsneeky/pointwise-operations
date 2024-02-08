import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sys
from pathlib import Path

def display_stripes(gray_level):
    # Create an empty array of size 256x256
    array = np.zeros((256, 256), dtype=np.uint8)

    # Define constants
    stripe_height = 16
    checkerboard_block_edge_length = 2

    # Calculate the number of stripes
    num_stripes = array.shape[0] // stripe_height

    # Alternate between checkerboard pattern and constant gray level
    for i in range(num_stripes):
        if i % 2 == 0:
            # create checkerboard on a stripe
            for j in range(i * stripe_height, (i + 1) * stripe_height, 1):
                for k in range(array.shape[1]):
                    if ((j // checkerboard_block_edge_length) + (k // checkerboard_block_edge_length)) % 2 == 0:
                        array[j, k] = 255
        else:
            # gray level
            array[i * stripe_height: (i + 1) * stripe_height, :] = gray_level

    # Display the array
    plt.imshow(array, cmap='gray', vmin=0, vmax=255)
    plt.axis('off')
    plt.show()

    return array

def gamma_correct_linear(linear_img: np.array, gamma: float):
    # original
    # y = 255 * (x / 255) ** gamma
    # apply inverted equation
    x = linear_img
    y = 255 * (x / 255) ** (1 / gamma)

    return y

def gamma_correct(gamma_corrected_img: np.array, gamma: float, desired_gamma: float):
    # convert gamma corrected image back to linear
    x = gamma_corrected_img
    linear_img = 255 * (x / 255) ** (gamma)
    
    # convert linear image back to gamma corrected
    y = gamma_correct_linear(linear_img, desired_gamma)
    
    return y
    
    
def main():
    initial_gray_level = 127
    # initial_image = display_stripes(initial_gray_level)
    
    matching_gray_level = 170
    # Display the image with the matching gray level
    matching_image = display_stripes(matching_gray_level)
    plt.imsave('matching_gray_level.png', matching_image, cmap='gray')

    # Print the matching gray level
    print("Matching Gray Level:", matching_gray_level)

    # Calculate gamma
    monitor_gamma = np.log(0.5) / np.log(matching_gray_level / 255)
    print("monitor gamma: ", monitor_gamma)
    
    im = Image.open('linear.tif')
    x = np.array(im)

    y = gamma_correct_linear(x, monitor_gamma)
    plt.imsave('linear_gamma_corrected.png', y, cmap='gray')
    
    im = Image.open('gamma15.tif')
    x = np.array(im)
    
    y = gamma_correct(x, 1.5, monitor_gamma)
    plt.imsave('gamma15_gamma_corrected.png', y, cmap='gray')
    
    
if __name__ == "__main__":
    main()