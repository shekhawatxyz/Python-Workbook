while True:
    a = float(input("Enter your age in human ears: "))
    d = 0
    if a <= 0:
        print("Enter a positive number.")
    if a >= 0 and a <= 2:
        d += 10.5 / 2 * a
        print(f"Your dog age is {d}")
        break
    else:
        a -= 2
        d += 10.5
        d = d + (a * 4)
        print(f"Your dog age is {d}")
        break
