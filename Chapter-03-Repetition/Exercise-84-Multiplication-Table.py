MIN = 1
MAX = 10

print("    ", end="")
for i in range(MIN, MAX + 1):
    print(f"{i:4d}", end="")
print()

for j in range(MIN, MAX + 1):
    print(f"{MIN * j:4d}", end="")
    for k in range(MIN, MAX + 1):
        print(f"{j * k:4d}", end="")
    print()
