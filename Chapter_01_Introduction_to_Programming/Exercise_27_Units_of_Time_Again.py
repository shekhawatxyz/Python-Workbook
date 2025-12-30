while True:
    t = int(input("Enter the amount of time in seconds: "))
    s = 0
    m = 0
    h = 0
    d = 0
    if t <= 0:
        print("Please enter a positive number")
    while t != 0:
        if t >= 24 * 3600:
            t = t - (24 * 3600)
            d += 1
        if t >= 3600:
            t = t - (3600)
            h += 1
        if t >= 60:
            t = t - 60
            m += 1
        if t >= 1:
            t = t - 1
            s += 1
    print(
        f"It's equivalent amount of time in DD:HH:MM:SS is {d:2d}:{h:2d}:{m:2d}:{s:2d} for now."
    )
    break
