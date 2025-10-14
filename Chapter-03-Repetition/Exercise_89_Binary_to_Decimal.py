b = input("Enter a binary number: ")
d = 0
l = len(b) - 1
for c in b:
    f = int(c) * 2**l
    d += f
    l -= 1
print(d)
