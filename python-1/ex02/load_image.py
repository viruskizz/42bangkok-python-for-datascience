import numpy as np
import matplotlib.image as mpimg


def ft_load(path: str) -> np.array:
    """ load an image from path and return numpy array """
    try:
        img = mpimg.imread(path)
        print("The shape of image is:", img.shape)
        return img
    except Exception as e:
        err_name = type(e).__name__
        err_msg = str(e)
        print(f"{err_name}: {err_msg}")
