# PV = nRT

while True:
    p = float(input("Please enter the pressure in kilopascals: "))
    v = float(input("Please enter the volume in liters: "))
    t = float(input("Please enter the temperature in degree celsius: "))
    t += 273.15
    if p <= 0 or v <= 0 or t <= 0:
        print(f"Please enter positive values.")
    r = 8.314
    n = (p * v) / (r * t)
    print(f"{n} is the amount of gas in moles.")
    break
