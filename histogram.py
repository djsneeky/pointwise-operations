import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sys
from pathlib import Path

def gen_hist(path: str):
    gray = plt.get_cmap('gray', 256)
    im = Image.open(path)
    x = np.array(im)

    plt.hist(x.flatten(), bins=np.linspace(0, 255, 256))
    plt.title("Histogram of " + path)
    plt.xlabel("pixel intensity")
    plt.ylabel("number of pixels")

    plt.savefig(Path(path).stem + '_hist.png')

def equalize(x: np.array):
    
    for pixel in x.flatten():
        z = pixel - 255 / 255

def main():
    gen_hist()
    
if __name__ == "__main__":
    main()