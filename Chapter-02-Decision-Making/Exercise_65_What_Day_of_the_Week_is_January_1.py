import math

y = int(input("Enter the year : "))

d = (
    (
        y
        + math.floor((y - 1) / 4)
        - math.floor((y - 1) / 100)
        + math.floor((y - 1) / 400)
    )
    & 7
) - 1
if d == 0:
    print(f"Sunday")
elif d == 1:
    print(f"Monday")
elif d == 2:
    print(f"Tuesday")
elif d == 3:
    print(f"Wednesday")
elif d == 4:
    print(f"Thursday")
elif d == 5:
    print(f"Friday")
else:
    print(f"Saturday")
