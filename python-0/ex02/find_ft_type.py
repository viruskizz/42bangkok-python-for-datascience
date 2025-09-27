def all_thing_is_obj(object: any) -> int:
    t = type(object)
    match t.__name__:
        case "list":
            print(f"{t.__name__.capitalize()} : {t}")
        case "tuple":
            print(f"{t.__name__.capitalize()} : {t}")
        case "set":
            print(f"{t.__name__.capitalize()} : {t}")
        case "dict":
            print(f"{t.__name__.capitalize()} : {t}")
        case "str":
            print(f"{object} is in the kitchen : {t}")
        case _:
            print("Type not fouund")
    return 42