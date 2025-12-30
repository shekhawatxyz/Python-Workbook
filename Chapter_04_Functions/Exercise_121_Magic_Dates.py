from Exercise_103_Days_in_a_Month import days_in_a_month


def main():
    for year in range(1901, 2000):
        two_digit_year = year % 100
        for month in range(1, 13):
            days = days_in_a_month(month, year)
            for day in range(1, days + 1):
                # latter_year = str(year)[2:0]
                if month * day == two_digit_year:
                    print(f"{day} {month} {year}")


main()
