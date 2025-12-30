while True:
    f = float(input("Enter the distance in feet: "))
    if f <= 0:
        print("Enter a positive number.")
    m = f / 5280
    y = f / 3
    i = f * 12
    print(f"The distance is {m} miles or {y} yards or {i} inches.")
    break
