d = []
o = 0
z = 0
for i in range(9):
    a = input("Enter the bits, enter blank to compute: ")
    if int(a) == 1:
        d.append(int(a))
        o += 1
    elif int(a) == 0:
        d.append(int(a))
        z += 1

    if len(d) == 8:
        if z % 2 != 0:
            d.append(1)
        else:
            d.append(0)
        print(d)
        break
