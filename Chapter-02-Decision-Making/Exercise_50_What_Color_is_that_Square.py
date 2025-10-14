a = input("Enter the position on the chessboard: ")
b = a[0].lower()
c = int(a[1])
s1 = ["a", "c", "e", "g"]
s2 = ["b", "d", "f", "h"]
if b in s1:
    if c % 2 == 0:
        print("white")
    elif c % 2 != 0:
        print("black")
if b in s2:
    if c % 2 != 0:
        print("white")
    elif c % 2 == 0:
        print("black")
