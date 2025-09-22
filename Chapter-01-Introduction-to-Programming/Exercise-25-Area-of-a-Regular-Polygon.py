import math

while True:
    n = int(input("Enter the number of sides of the regular polygon: "))
    s = int(input("Enter the length of the regular polygon: "))
    if s <= 0 or n <= 0:
        print("Enter a positive value.")
    area = (n * (s**2)) / (4 * math.tan(math.pi / n))
    print(f"The area of the polygon is {area}.")
    break
