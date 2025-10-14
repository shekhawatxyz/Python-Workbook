a = float(input("Enter the noise in db: "))
if a > 130:
    print("Louder than a jackhammer")
elif a == 130:
    print("As loud as a jackhammer")
elif a > 106:
    print("Between a gas lawnmower and a jackhammer")
elif a == 106:
    print("As loud as a gas lawnmower")
elif a > 70:
    print("Between a gas lawnmower and an alarm clock")
elif a == 70:
    print("As loud as an alarm clock")
elif a > 40:
    print("Between an alarm clock and a quiet room")
elif a == 40:
    print("As loud as a quiet room")
elif a < 40:
    print("Quieter than a quiet room")
else:
    print("Not in human range")
