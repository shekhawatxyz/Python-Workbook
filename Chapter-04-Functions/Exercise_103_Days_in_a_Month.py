def days_in_a_month(month, year):
    leap = 0
    assert month in range(1, 13)
    assert type(month) is int
    assert type(year) is int
    if year % 400 == 0:
        leap = 1
    elif year % 100 == 0:
        leap = 0
    elif year % 4 == 0:
        leap = 1
    else:
        leap = 0
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        if leap == 1:
            return 29
        else:
            return 28
    else:
        return 30


def main():
    a = int(input("Enter the month as an integer: "))
    b = int(input("Enter the year as an integer: "))
    print(days_in_a_month(a, b))


if __name__ == "__main__":
    main()
