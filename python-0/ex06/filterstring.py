import sys


def my_filter(fn, lst):
    if fn is None:
        return []
    return [x for x in lst if fn(x)]


def filterstring(s: str, n: int):
    words = s.split(" ")
    return my_filter(lambda w: len(w) > n, words)


def main():
    """ test function """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        s = sys.argv[1]
        for c in s:
            assert c.isalnum() or c == " ", "the argument are bad"
        n = int(sys.argv[2])
        f = filterstring(s, n)
        print(f)
    except Exception as e:
        err_name = type(e).__name__
        err_msg = str(e)
        print(f"{err_name}: {err_msg}")
    return 0


if __name__ == "__main__":
    main()
