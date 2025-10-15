from Exercise_103_Days_in_a_Month import days_in_a_month


def ordinalDate(year, month, day):
    assert type(year) is int
    assert type(month) is int
    assert type(day) is int

    d = 0
    # leap = 0
    # if year % 400 == 0:
    #     leap = 1
    # elif year % 100 == 0:
    #     leap = 0
    # elif year % 4 == 0:
    #     leap = 1
    # else:
    #     leap = 0
    for i in range(1, month):
        d += days_in_a_month(i, year)
    d = d + day
    d = f"{year}{d:03d}"
    return int(d)


def main():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    day = int(input("Enter the day: "))

    print(ordinalDate(year, month, day))


if __name__ == "__main__":
    main()
