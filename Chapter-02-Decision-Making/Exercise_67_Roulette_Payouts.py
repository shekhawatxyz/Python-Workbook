import random

# single number, red or black, odd or even without 0 or 00, 1-18 or 19-36
l = []
for i in range(37):
    l.append(str(i))
l.append("00")
r = random.choice(l)
red = [
    "1",
    "3",
    "5",
    "7",
    "9",
    "12",
    "14",
    "16",
    "18",
    "19",
    "21",
    "23",
    "25",
    "27",
    "30",
    "32",
    "34",
    "36",
]
print(f"The spin resulted in {r}...")
print(f"Pay {r}")
if r in red:
    print(f"Pay Red")
    if int(r) % 2 == 0:
        print(f"Pay Even")
    else:
        print(f"Pay Odd")
    if int(r) in range(1, 19):
        print("Pay 1 to 18")
    else:
        print("Pay 19 to 36")
elif r == "0" or r == "00":
    pass
else:
    print(f"Pay Black")
    if int(r) % 2 == 0:
        print(f"Pay Even")
    else:
        print(f"Pay Odd")
    if int(r) in range(1, 19):
        print("Pay 1 to 18")
    else:
        print("Pay 19 to 36")
