import math

s = input("Enter amount, enter a blank to stop: ")
a = 0
while s != "":
    a += float(s)
    s = input("Enter amount, enter a blank to stop: ")
c = int(input("Press 0 to pay via cash and 1 to pay via card or to pay online: "))
if c == 0:
    b = a * 100
    #    print(b)
    d = round((b % 5), 2)
    # print(d)
    if d < 2.5:
        b = math.floor(b)
        # print(b - d)
        print(f"${((b - d) / 100):.2f}")
    else:
        b = math.ceil(b)
        # print(b)
        print(f"${(b + 5 - d) / 100:.2f}")
else:
    print(f"${a:.2f}")
