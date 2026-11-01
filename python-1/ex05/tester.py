from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


def main():
    """ test crop and gray scale """
    try:
        src = "landscape.jpg"
        img = ft_load(src)
        ft_invert(img)
        ft_red(img)
        ft_green(img)
        ft_blue(img)
        ft_grey(img)
        print(ft_invert.__doc__)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
