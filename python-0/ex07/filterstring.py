import sys


def my_filter(fn, lst):
    """ filter list by function """
    if fn is None:
        return []
    return [x for x in lst if fn(x)]


def filterstring(s: str, n: int):
    """ filter string by len of word more than n """
    words = s.split(" ")
    return my_filter(lambda w: len(w) > n, words)


def validate_string(s: str) -> bool:
    """ validate string """
    for c in s:
        if not (c.isalnum() or c == " "):
            return False
    return True


def main():
    """ test function """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        s = sys.argv[1]
        assert validate_string(s), "the arguments are bad"
        n = int(sys.argv[2])
        f = filterstring(s, n)
        print(f)
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except ValueError:
        print("AssertionError: the arguments are bad")
    except Exception as e:
        # catch any other exception
        err_name = type(e).__name__
        err_msg = str(e)
        print(f"{err_name}: {err_msg}")
    return 0


if __name__ == "__main__":
    main()
