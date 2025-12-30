while True:
    d = float(input("Enter the number of days: "))
    h = float(input("Enter the number of hours: "))
    m = float(input("Enter the number of minutes: "))
    s = float(input("Enter the number of seconds: "))
    if d <= 0 or h <= 0 or m <= 0 or s <= 0:
        print("Enter positive values.")
    s *= 1
    m *= 60
    h *= 60 * 60
    d *= 24 * 60 * 60
    time = s + m + d + h
    print(f"The total time in seconds is {time}.")
    break
