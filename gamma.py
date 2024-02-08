import numpy as np
import matplotlib.pyplot as plt
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
    
def main():
    initial_gray_level = 127
    initial_image = display_stripes(initial_gray_level)
    
    matching_gray_level = 170
    # Display the image with the matching gray level
    matching_image = display_stripes(matching_gray_level)

    # Print the matching gray level
    print("Matching Gray Level:", matching_gray_level)

    # Calculate gamma
    gamma = np.log(0.5) / np.log(matching_gray_level / 255)
    print("gamma: ", gamma)
    
if __name__ == "__main__":
    main()