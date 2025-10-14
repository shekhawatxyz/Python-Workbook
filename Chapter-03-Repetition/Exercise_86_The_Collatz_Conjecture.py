import math
import random

b = int(input("Enter a positive integer: "))
d = [b]

while d[-1] != 1:
    if d[-1] % 2 == 0:
        d.append(math.floor(d[-1] / 2))
    else:
        d.append((d[-1] * 3) + 1)
print(d)
