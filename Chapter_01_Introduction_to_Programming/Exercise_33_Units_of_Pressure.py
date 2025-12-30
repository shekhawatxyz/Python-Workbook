while True:
    kp = float(input("Enter the pressure in kilopascals: "))
    psi = kp * 0.145038
    mmhg = kp * 7.50062
    atm = kp / 101.325
    print(
        f"pressure in psi - {psi}, mmhg - {mmhg}, atm - {atm} for the given value {kp}."
    )
    break
