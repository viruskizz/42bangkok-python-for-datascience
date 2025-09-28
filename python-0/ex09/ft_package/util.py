def count_in_list(lst: list, s) -> int:
    count = 0
    for x in lst:
        if x == s:
            count += 1
    return count