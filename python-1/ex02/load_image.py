import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def ft_load(path: str) -> np.array:
    try:
        img = mpimg.imread(path)
        print("The shape of image is:", img.shape)
        plt.imshow(img)
        # plt.axis("on")
        plt.show()
        return img
    except Exception as e:
        err_name = type(e).__name__
        err_msg = str(e)
        print(f"{err_name}: {err_msg}")