q = int(input("Enter the number to convert: "))
c = ""
while q != 0:
    r = q % 2
    c = c + str(r)
    q = q // 2
print(c)
