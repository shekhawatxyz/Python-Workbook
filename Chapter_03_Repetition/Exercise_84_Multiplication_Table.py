MIN = 1
MAX = 10

print("    ", end="")
for i in range(MIN, MAX + 1):
    print(f"{i:4d}", end="")
print()

for i in range(MIN, MAX + 1):
    print(f"{i:4d}", end="")
    for j in range(MIN, MAX + 1):
        print(f"{i * j:4d}", end="")
    print()
