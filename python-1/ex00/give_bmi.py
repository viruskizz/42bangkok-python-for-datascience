import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float])-> list[int | float]:
    """ Calculate list of height and weight to list of BMI """
    height_arr = np.array(height)
    weight_arr = np.array(weight)
    print(height_arr)
    bmi = weight_arr / (height_arr ** 2)
    return bmi.tolist()

def apply_limit(bmi: list[int | float], limit: int)-> list[bool]:
    """ Apply valid BMI range """
    bmi_arr = np.array(bmi)
    applied = bmi_arr > limit
    return applied.tolist()