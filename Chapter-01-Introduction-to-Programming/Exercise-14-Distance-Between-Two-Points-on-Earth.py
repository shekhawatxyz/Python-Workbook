import math

print(math.radians(90))
t1 = math.radians(float(input("Enter latitude 1: ")))
g1 = math.radians(float(input("Enter longitude 1: ")))
t2 = math.radians(float(input("Enter latitude 2: ")))
g2 = math.radians(float(input("Enter longitude 2: ")))
distance = 6371.01 * math.acos(
    (math.sin(t1) * math.sin(t2)) + (math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))
)
print(f"{distance}")
