import math

n = int(input("Enter an integer: "))
m = int(input("Enter an integer: "))
d = min(n, m)
while n % d != 0 or m % d != 0:
    d -= 1
print(d)
