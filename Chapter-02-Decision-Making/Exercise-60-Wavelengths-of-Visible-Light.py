a = float(input("Enter the wavelength please: "))
if a > 750:
    print("Outside the visible spectrum")
elif a >= 620:
    print("Red")
elif a >= 590:
    print("Orange")
elif a >= 570:
    print("Yellow")
elif a >= 495:
    print("Green")
elif a >= 450:
    print("Blue")
elif a >= 380:
    print("Violet")
else:
    print("Outside the visible spectrum")
