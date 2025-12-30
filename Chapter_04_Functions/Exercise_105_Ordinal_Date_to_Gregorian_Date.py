import calendar
from Exercise_104_Gregorian_Date_to_Ordinal_Date import ordinalDate
from Exercise_103_Days_in_a_Month import days_in_a_month


def gregorianDate(a):
    b = str(a)[4:]
    b = int(b)
    c = str(a)[0:4]
    c = int(c)
    for i in range(1, 13):
        if b > days_in_a_month(i, c):
            b -= days_in_a_month(i, c)
        else:
            f = f"{c} {i:02d} {b:02d}"
            return f


def check_date(time, extra):
    time = str(time)
    year = time[0:4]
    y = int(year)
    date = time[4:]
    d = int(date)
    new_d = d + extra

    while True:
        if calendar.isleap(y):
            if new_d > 366:
                new_d -= 366
                y += 1
                continue
            else:
                f = f"{y}{new_d:03d}"
                return f
        else:
            if new_d > 365:
                new_d -= 365
                y += 1
                continue
            else:
                f = f"{y}{new_d:03d}"
                return f


a = input("Enter the ordinal date: ")
b = gregorianDate(a)
print(f"So {b} in gregorian terms")
# a1 = input("Enter the year: ")
# a2 = input("Enter the month: ")
# a3 = input("Enter the day: ")
# b = ordinalDate(int(a1), int(a2), int(a3))
# print(b)
e = input("Enter the extra time: ")
new_o = check_date(str(a), int(e))

new_g = gregorianDate(new_o)
print(f"The new date in gregorian terms is {new_g}")
