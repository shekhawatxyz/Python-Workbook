d = 3
a = 2
b = 3
c = 4
for i in range(15):
    j = 2 * i
    # print(i)
    l = (-1) ** i
    # print(l)
    # print(f"{(4 * (l))}")
    d += (4 * (l)) / ((a + j) * (b + j) * (c + j))
print(d)
