m = float(input("Enter the scale: "))
d = [
    "Micro",
    "Very Minor",
    "Minor",
    "Light",
    "Moderate",
    "Strong",
    "Major",
    "Great",
    "Meteoric",
]

if m < 2.0:
    print(f"{d[0]}")
elif m < 3.0:
    print(f"{d[1]}")
elif m < 4.0:
    print(f"{d[2]}")
elif m < 5.0:
    print(f"{d[3]}")
elif m < 6.0:
    print(f"{d[4]}")
elif m < 7.0:
    print(f"{d[5]}")
elif m < 8.0:
    print(f"{d[6]}")
elif m < 10.0:
    print(f"{d[7]}")
elif m >= 10.0:
    print(f"{d[8]}")
