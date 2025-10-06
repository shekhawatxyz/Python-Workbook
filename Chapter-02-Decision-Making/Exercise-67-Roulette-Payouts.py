import random

# single number, red or black, odd or even without 0 or 00, 1-18 or 19-36
l = []
for i in range(37):
    l.append(str(i))
l.append("00")

print(random.choice(l))
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
