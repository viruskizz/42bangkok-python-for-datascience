import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    arr = np.array(family)
    new_arr = arr[start:end] # [row_start:row_end, col_start:col_end]
    print(f"My shape is : {arr.shape}")
    print(f"My new shape is : {new_arr.shape}")
    return new_arr
