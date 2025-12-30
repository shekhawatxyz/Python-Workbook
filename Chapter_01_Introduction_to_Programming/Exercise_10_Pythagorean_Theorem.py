while True:
    a = float(input("Enter shorter side a: "))
    b = float(input("Enter shorter side b: "))
    if a <= 0 or b <= 0:
        print("Enter positive values please.")
        continue
    c = (a**2) + (b**2)
    print(f"{c**0.5}")
    break
