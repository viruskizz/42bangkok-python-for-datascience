import os


def ft_tqdm(lst: range) -> None:
    """ progress loading bar with yield """
    size = os.get_terminal_size()
    block = size.columns - 20
    total = len(lst)
    for i in lst:
        poc = i / total
        bar = "=" * int(poc * block)
        sp = " " * int((1 - poc) * block)
        percent = f"{int(poc * 100) + 1}%"
        progress = f"{i + 1}/{total}"
        print(f"\r{percent:>4}|[{bar}>{sp}]| {progress}", end="", flush=True)
        yield i
