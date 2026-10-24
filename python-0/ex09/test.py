"""Manual tests for count_in_list."""

from ft_package.util import count_in_list


def main():
    """Print actual and expected results."""
    print(count_in_list(["toto", "tata", "toto"], "toto"), "expected: 2")
    print(count_in_list(["toto", "tata", "toto"], "tutu"), "expected: 0")
    print(count_in_list([], "toto"), "expected: 0")
    print(count_in_list([1, 2, 1, 3], 1), "expected: 2")


if __name__ == "__main__":
    main()