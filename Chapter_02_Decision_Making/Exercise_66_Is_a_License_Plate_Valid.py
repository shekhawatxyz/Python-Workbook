a = input("Enter the license plate: ")
al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nl = "1234567890"
a1 = 0
a2 = 0
n1 = 0
n2 = 0
if len(a) == 6:
    if a[0] in al and a[1] in al and a[2] in al:
        a1 = 1
    if a[3] in nl and a[4] in nl and a[5] in nl:
        n1 = 1
    if a1 == 1 and n1 == 1:
        print("Old timey number plate")
    else:
        print("Wrong format!")
elif len(a) == 7:
    if a[0] in nl and a[1] in nl and a[2] in nl and a[3] in nl:
        n2 = 1
    if a[4] in al and a[5] in al and a[6] in al:
        a2 = 1
    if a2 == 1 and n2 == 1:
        print("New timey number plate")
    else:
        print("Wrong format!")
else:
    print("Wrong format!")
