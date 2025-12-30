# one cup = 16 tablespoons or 48 x
# one tablespoon = 3 teaspoons or 3x
# one teaspoon = x
def spoon_convertor(num, unit):
    # num = 90
    # unit = "teaspoons"
    universal_unit = 1
    if unit == "teaspoons":
        universal_unit = 1
    elif unit == "tablespoons":
        universal_unit = 3
    elif unit == "cups":
        universal_unit = 48
    else:
        raise ValueError
    total_volume = num * universal_unit
    cups = 0
    teaspoons = 0
    tablespoons = 0
    while total_volume >= 48:
        if total_volume < 48:
            break
        total_volume -= 48
        cups += 1
        print(total_volume)
    while total_volume >= 9:
        if total_volume < 9:
            break
        total_volume -= 9
        tablespoons += 1
    while total_volume < 9:
        if total_volume < 1:
            break
        total_volume -= 1
        teaspoons += 1
    return f"{cups} cups, {tablespoons} tablespoons and {teaspoons} teaspoons."


def main():
    num = int(input("Enter the number of units:"))
    unit = input("Enter the kind of units, teaspoons, tablespoons or cups: ")
    print(spoon_convertor(num, unit))


if __name__ == "__main__":
    main()
