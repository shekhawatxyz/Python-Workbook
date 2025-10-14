import calendar

y = int(input("Enter the year: "))
m = int(input("Enter the month: "))
d = int(input("Enter the day: "))
l = 0
if calendar.isleap(y):
    l = 1
if m == 4 or m == 6 or m == 9 or m == 11:
    if d == 30:
        print(f"{y} {m + 1} {1}")
    elif d < 30:
        print(f"{y} {m} {d + 1}")
elif m == 12:
    if d == 31:
        print(f"{y + 1} {1} {1}")
elif m == 2:
    if l == 1:
        if d == 29:
            print(f"{y} {m + 1} {1}")
        elif d < 29:
            print(f"{y} {m} {d + 1}")
    else:
        if d == 28:
            print(f"{y} {m + 1} {1}")
        elif d < 28:
            print(f"{y} {m} {d + 1}")
else:
    if d < 31:
        print(f"{y} {m} {d + 1}")
    elif d == 31:
        print(f"{y} {m + 1} {1}")
