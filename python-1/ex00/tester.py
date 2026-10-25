from give_bmi import give_bmi, apply_limit


def main():
    """Test BMI calculations and invalid input handling."""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

    try:
        height = [2.71, 1.15, "invalid"]
        weight = [165.3, 38.4, 50]
        bmi = give_bmi(height, weight)
        print("This should not print, as an exception is expected.")
    except (TypeError, ValueError) as e:
        print(e)


if __name__ == "__main__":
    main()
