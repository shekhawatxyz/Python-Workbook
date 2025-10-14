import math

while True:
    r = float(input("Enter the radius "))
    if r <= 0:
        print("Enter a positive number.")
    area = math.pi * (r**2)
    volume = math.pi * (4 / 3) * (r**3)
    print(f"The area is {area} and the volume is {volume}")
    break
