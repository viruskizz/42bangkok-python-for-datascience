def count_in_list(lst: list, s) -> int:
    """ count number of target word """
    count = 0
    for x in lst:
        if x == s:
            count += 1
    return count
