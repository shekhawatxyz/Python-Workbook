import math

x1 = int(input("Enter the first x-coordinate: "))
y1 = int(input("Enter the first y-coordinate: "))
x = [x1]
y = [y1]
while True:
    xn = input("Enter the next x-coordinate (blank to quit) : ")
    if xn == "":
        break
    else:
        xn = int(xn)
        yn = int(input("Enter the next y-coordinate: "))
        x.append(xn)
        y.append(yn)
x.append(x1)
y.append(y1)
d = 0
if len(x) < 2 or len(y) < 2:
    print("Can't give the perimeter of a point")
for idx, char in enumerate(x):
    if idx > 0:
        d += math.sqrt(((x[idx] - x[idx - 1]) ** 2) + ((y[idx] - y[idx - 1]) ** 2))
print(d)
