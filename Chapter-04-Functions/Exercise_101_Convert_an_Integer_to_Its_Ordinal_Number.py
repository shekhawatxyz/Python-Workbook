def ordinal(a):
    assert a in range(1, 13)
    o = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth",
    ]
    return o[a - 1]


def main():
    a = int(input("Enter a number between 1 and 12: "))

    print(ordinal(a))


if __name__ == "__main__":
    main()
