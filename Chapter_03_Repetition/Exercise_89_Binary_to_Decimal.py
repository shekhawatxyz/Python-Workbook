b = input("Enter a binary number: ")
# b = "1010100"
d = 0
l = len(b) - 1
for c in b:
    f = int(c) * 3**l
    d += f
    l -= 1
print(d)

# 348 - (10^2*3)+(10^1*4)+(10^0*8)
# 348 -
