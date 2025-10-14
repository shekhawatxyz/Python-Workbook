import math

while True:
    r = float(input("Enter the radius of the cylinder: "))
    h = float(input("Enter the height of the cylinder: "))
    if r <= 0 or h <= 0:
        print("Please enter a positive number.")
    a = math.pi * (r**2)
    print(f"The volume of a cylinder is {a * h}.")
    break
