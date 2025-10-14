import math


def hypotenuse(a, b):
    assert b > 0, "Side must be a positive integer"
    assert a > 0, "Side must be a positive integer"
    return math.sqrt((a**2) + (b**2))


def main():
    a = int(input("Enter the first side: "))
    b = int(input("Enter the first side: "))
    print(f"The hypotenuse is {hypotenuse(a, b)}")


if __name__ == "__main__":
    main()
