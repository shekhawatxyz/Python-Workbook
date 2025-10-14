n = int(input("Enter a number: "))
import math

f = 2

while f <= n:
    if n % f == 0:
        n = math.floor(n / f)
        print(f)
    else:
        f += 1
