import numpy as np


def validate_list(input_list: list) -> bool:
    """ Validate if the input list is a list of numbers """
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    if len(input_list) == 0:
        raise ValueError("Input list must not be empty")
    for item in input_list:
        if not isinstance(item, (int, float)):
            raise TypeError("All items in the list must be int or float")
        if item <= 0:
            raise ValueError("All items in the list must be greater than zero")
    return True


def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[int | float]:
    """ Calculate list of height and weight to list of BMI """
    # Validate input lists
    validate_list(height)
    validate_list(weight)
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same length")
    # Operations
    height_arr = np.array(height)
    weight_arr = np.array(weight)
    bmi = weight_arr / (height_arr ** 2)
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """ Apply valid BMI range """
    if not isinstance(bmi, list):
        raise TypeError("BMI must be a list")
    for i in bmi:
        if not isinstance(i, (int, float)):
            raise TypeError("BMI list must contain only int or float values")
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer")
    bmi_arr = np.array(bmi)
    applied = bmi_arr > limit
    return applied.tolist()
