import sys


def get_alpha_type(c: str):
    """ return character type """
    if c == " ":
        return "sp"
    elif c.isdigit():
        return "digit"
    elif c.isupper():
        return "upper"
    elif c.islower():
        return "lower"
    else:
        return "punc"


def building(s: str) -> None:
    """ count type of alphabets """
    counter = {
        "sp": 0,
        "digit": 0,
        "upper": 0,
        "lower": 0,
        "punc": 0,
    }
    for c in s:
        tp = get_alpha_type(c)
        counter[tp] += 1
    print(f"the text contains {len(s)} characters")
    print(f'{counter["upper"]} upper letters')
    print(f'{counter["lower"]} lower letters')
    print(f'{counter["punc"]} punctuation marks')
    print(f'{counter["sp"]} spaces')
    print(f'{counter["digit"]} digits')


def main():
    """ test function """
    try:
        if len(sys.argv) == 2:
            data = sys.argv[1]
        elif len(sys.argv) == 1:
            inpt = sys.stdin.read()
            inpt = inpt[:-1] + " "  # replace return caret with space
            data = inpt.split("\n")[-1]  # Get only last line
        else:
            msg = "AssertionError: more than one argument is provided"
            raise Exception(msg)
        building(data)
    except Exception as e:
        print(e)
    return 0


if __name__ == "__main__":
    main()
