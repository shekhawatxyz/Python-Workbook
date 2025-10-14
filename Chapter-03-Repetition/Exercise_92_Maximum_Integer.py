import random

a = random.randint(1, 100)
print(a)
big = a
z = 0
for d in range(99):
    f = random.randint(1, 100)
    if f > big:
        big = f
        print(f, end="")
        print("<== Update")
        z += 1
    else:
        print(f)
print(f"The maximum value found was {big}.")
print(f"The maximum value was updated {z} times.")
