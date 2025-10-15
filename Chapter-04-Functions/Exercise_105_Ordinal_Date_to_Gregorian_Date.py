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


# def main():
#     # a = int(input("Enter the ordinal date: "))
#     a = "2024061"
#     return gregorianDate(a)


# b = main()
b = gregorianDate("2024061")
print(len(b))
time = "2024367"
print(time)
year = time[0:4]
print(year)
y = int(year)
date = time[4:]
d = int(date)
print(d)
extra = 300
new_d = d + extra
print(new_d)

while True:
    if calendar.isleap(y):
        if new_d > 366:
            new_d -= 366
            y += 1
            continue
        else:
            print(f"leap year loop")
            print(f"{y}{new_d}")
            break
    else:
        if new_d > 365:
            new_d -= 365
            y += 1
            continue
        else:
            print("non leap year loop")
            print(f"{y}{new_d}")
            break


print(type(b))
# print(type(nd))

# print(gregorianDate(nd))
# ordinalDate()
