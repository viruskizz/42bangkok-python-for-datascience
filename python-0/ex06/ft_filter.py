from typing import Callable, Iterable

def ft_filter(fn: Callable, lst: Iterable) -> list:
    """ My customize filter that clone from filter build-in-function """
    assert type(lst).__name__ == "list", "argument is not iterable"
    if fn is None:
        return lst
    assert type(fn).__name__ == "function", "argument is not function"
    return [x for x in lst if fn(x)]

def main():
    nums = [1, 2, 3, 4, 5, 6]
    filt = ft_filter(lambda x: x, nums)
    print(filt)

if __name__ == "__main__":
    main()