from typing import Iterable


def ft_filter(fn, lst: Iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    for x in lst:
        if fn is None:
            if x:
                yield x
        elif fn(x):
            yield x


def main():
    """ test function """
    nums = [1, 2, 3, 4, 5, 6]
    ft_filt = ft_filter(lambda x: x, nums)
    # ft_filt = ft_filter(None, [0, 1, "", "hi", False, True])

    print("=== ft_filter ===")
    print(ft_filter.__doc__)
    print(list(ft_filt))


if __name__ == "__main__":
    main()
