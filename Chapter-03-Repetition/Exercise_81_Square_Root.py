# x = int(input("Enter the number: "))
import math

x = 16
g = x / 2
# print(g)
c = (g * g) - x
# print(c)
d = 10 ** (-12)
# print(d)
while c > ((10) ** (-12)):
    # print(c)
    g = (g + (x / g)) / 2
    c = (g * g) - x
    if c == 0:
        break
print(f"The convergence happened at {g}.")
