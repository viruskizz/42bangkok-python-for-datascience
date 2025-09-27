def NULL_not_found(object: any) -> int:
    t = type(object)
    tn = t.__name__
    if object is None:
        print(f"Nothing: {object} {t}")
    elif tn == "float" and object != object:
        print(f"Cheese: {object} {t}")
    elif tn == "int" and object == 0:
        print(f"Zero: {object} {t}")
    elif tn == "str" and object == "":
        print(f"Empty: {t}")
    elif tn == "bool" and object == False:
        print(f"Fake: {object} {t}")
    else:
        print("Type not Found")
        return 1
    return 0