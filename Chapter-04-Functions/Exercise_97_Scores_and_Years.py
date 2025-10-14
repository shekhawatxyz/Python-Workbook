def total_years(s, y):
    assert s >= 0
    assert y >= 0
    return (s * 20) + y


def main():
    s = int(input("Enter the number of scores: "))
    y = int(input("Enter the number of years: "))
    print(f"Total years: {total_years(s, y)}")


if __name__ == "__main__":
    main()
