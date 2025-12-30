import math

while True:
    num_rings = int(input("Enter the number of rings in the spiral: "))
    first_diameter = int(input("Enter the average diameter of the first ring: "))
    last_diameter = int(input("Enter the average diamter of the largest ring: "))
    if num_rings <= 0 or first_diameter <= 0 or last_diameter <= 0:
        print("Enter a positive number please.")
    length = math.pi * num_rings * ((first_diameter + last_diameter) / 2)
    l = float(length)
    print(f"The length of the spiral is {l:.1f}")
    break
