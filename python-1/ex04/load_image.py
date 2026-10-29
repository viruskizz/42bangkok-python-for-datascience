import numpy as np
import matplotlib.image as mpimg
# import matplotlib.pyplot as plt


def ft_load(path: str) -> np.ndarray:
    """ load an image to numpy array """
    img = mpimg.imread(path)
    return img
