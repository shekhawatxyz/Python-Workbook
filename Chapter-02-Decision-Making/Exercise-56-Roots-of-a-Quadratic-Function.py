import math

a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
c = int(input("Enter the value for c: "))

d0 = (b**2) - (4 * a * c)
if d0 < 0:
    print("Negative, no real roots")
elif d0 == 0:
    print(f"the real root is {-b / (2 * a)}")
else:
    d = math.sqrt((b**2) - (4 * a * c))
    root1 = ((-b) + d) / (2 * a)
    root2 = ((-b) - d) / (2 * a)
    print(f"The two real roots are {root1} and {root2}")
