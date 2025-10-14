m = input("Enter the month: ")
d = int(input("Enter the date: "))
if m.capitalize() == "December":
    if d < 22:
        print("Sagittarius")
    else:
        print("Capricorn")
elif m.capitalize() == "January":
    if d < 20:
        print("Capricorn")
    else:
        print("Aquarius")
elif m.capitalize() == "February":
    if d < 19:
        print("Aquarius")
    else:
        print("Pisces")
elif m.capitalize() == "March":
    if d < 22:
        print("Pisces")
    else:
        print("Aries")
elif m.capitalize() == "April":
    if d < 20:
        print("Aries")
    else:
        print("Taurus")
elif m.capitalize() == "May":
    if d < 21:
        print("Taurus")
    else:
        print("Gemini")
elif m.capitalize() == "June":
    if d < 21:
        print("Gemini")
    else:
        print("Cancer")
elif m.capitalize() == "July":
    if d < 23:
        print("Cancer")
    else:
        print("Leo")
elif m.capitalize() == "August":
    if d < 23:
        print("Leo")
    else:
        print("Virgo")
elif m.capitalize() == "September":
    if d < 23:
        print("Virgo")
    else:
        print("Libra")
elif m.capitalize() == "October":
    if d < 23:
        print("Libra")
    else:
        print("Scorpio")
elif m.capitalize() == "November":
    if d < 22:
        print("Scorpio")
    else:
        print("Stagittarius")
