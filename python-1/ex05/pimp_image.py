import numpy as np
import matplotlib.pyplot as plt


def validate_image_array(array: np.ndarray) -> None:
    """ Validate that the input is a 3D numpy array with 3 channels (RGB) """
    if not isinstance(array, np.ndarray):
        raise ValueError("Input must be a numpy array")
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError(
            "Input array must be a 3D array with 3 channels (RGB)"
        )


def ft_invert(array) -> np.ndarray:
    """ Inverts the color of the image received. """
    validate_image_array(array)
    inverted_array = 255 - array
    plt.imshow(inverted_array)
    plt.show()
    return inverted_array


def ft_red(array) -> np.ndarray:
    """ Select only red channel from array representing an image """
    validate_image_array(array)
    new_array = np.copy(array)
    new_array[:, :, 1] = 0
    new_array[:, :, 2] = 0
    plt.imshow(new_array)
    plt.show()
    return new_array


def ft_green(array) -> np.ndarray:
    """ Select only green channel from array representing an image """
    validate_image_array(array)
    new_array = np.copy(array)
    new_array[:, :, 0] = 0
    new_array[:, :, 2] = 0
    plt.imshow(new_array)
    plt.show()
    return new_array


def ft_blue(array) -> np.ndarray:
    """ Select only blue channel from array representing an image """
    validate_image_array(array)
    new_array = np.copy(array)
    new_array[:, :, 0] = 0
    new_array[:, :, 1] = 0
    plt.imshow(new_array)
    plt.show()
    return new_array


def ft_grey(array) -> np.ndarray:
    """ Convert a numpy array representing an image to grayscale """
    validate_image_array(array)
    new_array = np.copy(array)
    new_array[:, :, 1] = array[:, :, 0]
    new_array[:, :, 2] = array[:, :, 0]
    plt.imshow(new_array)
    plt.show()
    return new_array
