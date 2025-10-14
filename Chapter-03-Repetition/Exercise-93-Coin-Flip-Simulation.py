import random

o = ["H", "T"]
d = 0
for i in range(10):
    a = 0
    c = True
    t = 0
    h = 0
    while True:
        f = random.choice(o)
        if t == 3 or h == 3:
            print(f"({a} flips)")
            d += a
            break
        if f == "H":
            a += 1
            h += 1
            t = 0
            print(f, end=" ")
        else:
            a += 1
            t += 1
            h = 0
            print(f, end=" ")
print(f"On average, {d / 10} flips were needed")
