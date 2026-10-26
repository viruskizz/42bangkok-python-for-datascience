from load_image import ft_load
import matplotlib.pyplot as plt


def gray_scale(img):
    """ Select the red channel as a 2D intensity array """
    return img[:, :, 0]


def crop(img, y_start: int, y_end: int, x_start: int, x_end: int):
    """ crop the image to the specified coordinates """
    return img[y_start:y_end, x_start:x_end]


def main():
    """ test crop and gray scale """
    try:
        src = "animal.jpeg"
        img = ft_load(src)
        print(f"The shape of image is: {img.shape}")
        print(img)
        cropped_img = crop(img, 100, 500, 400, 800)
        gray_img = gray_scale(cropped_img)
        print(f"New shape after slicing: {gray_img.shape}")
        print(gray_img)
        plt.imshow(gray_img, cmap="gray")
        plt.axis("on")
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
