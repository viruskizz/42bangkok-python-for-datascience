import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    arr = np.array(family)
    if arr.ndim != 2:
        raise ValueError("Input array must be 2-dimensional")
    new_arr = arr[start:end]  # [row_start:row_end, col_start:col_end]
    print(f"My shape is : {arr.shape}")
    print(f"My new shape is : {new_arr.shape}")
    return new_arr.tolist()
