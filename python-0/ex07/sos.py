import sys


def get_code(s: str) -> str:
    """ mapping character to morse code """
    MORSE = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }
    return MORSE[s.upper()]


def encoding(s: str) -> str:
    """ convert string to morse code string """
    codes = [get_code(c) for c in s]
    return " ".join(codes)


def main():
    """ test function """
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        s = sys.argv[1]
        for c in s:
            assert c.isalnum() or c == " ", "the argument are bad"
        m = encoding(s)
        print(m)
    except Exception as e:
        err_name = type(e).__name__
        err_msg = str(e)
        print(f"{err_name}: {err_msg}")


if __name__ == "__main__":
    main()
